#!/usr/bin/env python3
"""Offline grader for the skill evals (see evals/README.md).

  python3 evals/grade.py list                 validate every case and print the table
  python3 evals/grade.py prompt CASE_ID       print the prompt of a case, fixtures appended
  python3 evals/grade.py grade OUTDIR         grade saved outputs OUTDIR/<case-id>.md
                                              (+ optional OUTDIR/<case-id>.meta.json)
                                              exit 0 only if all cases were graded and passed;
                                              1 a check failed (highest priority), 3 an output is
                                              missing, 2 isolation is unverified

No network and no LLM. Automatic results go to OUTDIR/automatic.json; the manual
rubric scores are a separate file, OUTDIR/manual.json, filled in by a person.
Needs PyYAML (pip install pyyaml).
"""
import argparse
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")

EVALS = Path(__file__).resolve().parent
ROOT = EVALS.parent
SKILLS = ROOT / "skills"
CASES = EVALS / "cases"
FIXTURES = EVALS / "fixtures"
KINDS = {"main", "vague", "trap", "standalone"}

# Requirement-style codes: US-02, AC-01.2, BR-09, NFR-SEC-01
ID_RE = re.compile(r"(?<![A-Za-z0-9-])[A-Z]{2,5}(?:-[A-Z]{2,5})?-\d+(?:\.\d+)?(?![\d])")
RANGE_RE = re.compile(r"\b([A-Z]{2,5}(?:-[A-Z]{2,5})?)-(\d+)\s*(?:to|through|\.\.\.?|\u2026)\s*(?:\1-)?(\d+)\b")
UNIT = (r"(?:seconds?|secs?|minutes?|mins?|hours?|days?|weeks?|months?|years?|attempts?|tries|times|"
        r"passwords?|characters?|percent|users?|failed|wrong|ms)")
NUMBER_WORD_RE = re.compile(
    r"\b(two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|fifteen|twenty|thirty|forty|fifty|"
    r"sixty|hundred|thousand)\b(?=[\s-]+" + UNIT + r"\b)", re.I)
NUMBER_WORDS = {w: n for w, n in zip(
    "two three four five six seven eight nine ten eleven twelve fifteen twenty thirty forty fifty sixty "
    "hundred thousand".split(), [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 20, 30, 40, 50, 60, 100, 1000])}
REF_NUMBER_RE = re.compile(r"(?i)\b(?:questions?|sections?|findings?|items?|rows?|points?|steps?|checks?|clauses?|"
                           r"criteri(?:on|a)|tables?|lines?|scenarios?|cases?|c\u00e2u h\u1ecfi|c\u00e2u)\s+\d+(?:\.\d+)*(?:\s*(?:-|to)\s*\d+(?:\.\d+)*)?|#\d+")
CONCRETE_AMOUNT_RE = re.compile(r"\d+(?:[.,]\d+)?\s*(?:%|ms|s\b|sec|secs|seconds?|mins?|minutes?|hours?|days?|"
                                r"giây|phút|giờ|ngày)", re.I)
DASHES_RE = re.compile("[\u2010\u2011\u2012\u2013\u2212]")  # hyphen look-alikes: US\u201199 is the code US-99
ISO_DATE_RE = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
MONTH = (r"(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|"
         r"Sep(?:t(?:ember)?)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)")
EXAMPLE_DATA_RE = re.compile(
    r"\b\d{1,2}:\d{2}(?::\d{2})?(?:\s?[ap]m\b)?"                                  # 09:00, 14:30, 9:00 am
    r"|\b\d{1,2}(?:st|nd|rd|th)?\s+(?:of\s+)?" + MONTH + r"\b(?:,?\s+\d{4})?"     # 10 Nov, 3rd March 2027
    r"|\b" + MONTH + r"\s+\d{1,2}(?:st|nd|rd|th)?\b(?:,?\s+\d{4})?"               # Nov 10, March 3rd
    r"|\b\d+\s*(?:h|hours?)\s*\d{1,2}\s*(?:min|minutes?)\b"                         # "23 h 59 min" as a boundary example
    r"|\b00\s*(?:minutes?|mins?|seconds?|secs?)\b")                                   # "24 hours 00 minutes"
VARIABLE_STEP_RE = re.compile(r"\b[A-Za-z]\s?[-+]\s?\d{1,2}\b(?![\d:.])")  # N-1, N+1: a parameter, not a figure
COUNTER_RESET_RE = re.compile(r"(?i)\b(?:resets?|resetting|counter|count)\b[^.\n]{0,30}?\b(?:to|is|at|=)\s*0\b")
QUOTED_RE = re.compile(r'"[^"\n]*"|\u201c[^\u201d\n]*\u201d')
GWT_RE = re.compile(r"\b(?:given|when|then)\b|^\s*(?:[-*]\s*)?(?:and|but)\b", re.I)
# "F2", "Q4", "A1", "AC3", "AC 3": labels of findings, questions, assumptions and criteria the answer numbers itself
LABEL_RE = re.compile(r"\b(?:[FQA]\d{1,3}|AC\s?\d{1,3}|P\d)\b")  # P1, P2: patient 1, patient 2
PERCENTILE_RE = re.compile(r"(?i)\bp\d{2}(?:\.\d)?\b")  # p95 names a way to measure, it sets no value
OWN_COUNT_RE = re.compile(r"(?i)\b\d+\s+(?:stories|story|user stories|ACs?|acceptance criteria|questions?|c\u00e2u h\u1ecfi|c\u00e2u)\b")  # "split into 4 stories"
ZERO_PADDED_RE = re.compile(r"\b00\s*(?:minutes?|mins?|seconds?|secs?)\b")  # "24 h 00 min"
VARIABLE_RANGE_RE = re.compile(r"\b\d+\s+to\s+[A-Za-z]\b(?:\s?[-+]\s?\d{1,2}\b)?")  # "attempts 1 to N-1"
NUMBER_RE = re.compile(r"\d+(?:[.,]\d+)?")
PATH_TOKEN_RE = re.compile(
    r"(?<![\w/.-])((?:[a-z0-9-]+/)?(?:references|templates|scripts)/[A-Za-z0-9_./-]*[A-Za-z0-9_])")
LOOKUP_FAILURE_RE = re.compile(
    r"(?:cannot|can't|could not|couldn't|unable to|failed to)\s+(?:find|read|open|load|access|locate)"
    r"|file not found|no such file|does not exist|doesn't exist", re.I)
NEGATION_RE = re.compile(r"(?i)\b(?:not|never|cannot|unable|without)\b|n't\b")
HEAD_RE = re.compile(r"^\s{0,3}#{1,6}\s+(.*?)\s*#*\s*$")
BOLD_LABEL_RE = re.compile(r"^\s*\*\*([^*]+?)(?::\*\*|\*\*\s*:)\s*(.*)$")
BOLD_PAREN_RE = re.compile(r"^\s*\*\*([^*]+?)\*\*\s*\(([^()]*)\)\s*$")  # `**Acceptance criteria** (rule-list form)`
BOLD_LINE_RE = re.compile(r"^\s*\*\*([^*]+?)\*\*\s*$")
HEAD_NUMBER_RE = re.compile(r"^\s*(?:\d+(?:\.\d+)+[.)]?\s+|\d+[.)]\s*)")  # "3. Findings", "11.2 What is still missing"
BOLD_RE = re.compile(r"(\*\*|__)(?=\S)([^\n]+?)(?<=\S)\1")
ITALIC_STAR_RE = re.compile(r"(?<![\w*])\*(?=[^\s*])([^*\n]+?)(?<=[^\s*])\*(?![\w*])")
ITALIC_UNDERSCORE_RE = re.compile(r"(?<![\w_])_(?=[^\s_])([^_\n]+?)(?<=[^\s_])_(?![\w_])")
REQ_PREFIXES = {"US", "AC", "BR", "FR", "NFR", "TC", "UC", "REQ", "GOAL", "SR", "RV", "RR", "OQ", "GAP",
                "ASM", "DEP", "EPIC", "UAT", "SYS", "BG"}
EXAMPLE_MARKER_RE = re.compile(
    r"(?i)(?:\b(?:such as|for example|for instance|like|including)\b|\be\.?g\.?(?=[\s,])|"
    r"\bv\u00ed d\u1ee5(?: nh\u01b0)?\b|\bch\u1eb3ng h\u1ea1n(?: nh\u01b0)?\b)[^.;:!?\n]{0,60}$")
# Section names that mean the same thing; the key is what the case file asks for.
SECTION_ALIASES = {"questions needing an answer": ["open questions"]}
BLOCK_START_RE = re.compile(r"^\s*(\||[-*+]\s|\d+[.)]\s)")
SEPARATOR_RE = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?\s*$")
VERDICT_WORDS = {"ready", "not ready", "conditional"}  # `**Conditional**: ...` is text, not a section
DEFAULT_VAGUE = ["fast", "quick", "quickly", "easy", "easily", "user-friendly", "friendly",
                 "intuitive", "smart", "suitable", "appropriate",
                 "nhanh", "dễ dùng", "thân thiện", "phù hợp"]
VIETNAMESE_CHARS = set("ăâđêôơưàáạảãằắặẳẵầấậẩẫèéẹẻẽềếệểễìíịỉĩòóọỏõồốộổỗờớợởỡùúụủũừứựửữỳýỵỷỹ"
                       "ĂÂĐÊÔƠƯÀÁẠẢÃẰẮẶẲẴẦẤẬẨẪÈÉẸẺẼỀẾỆỂỄÌÍỊỈĨÒÓỌỎÕỒỐỘỔỖỜỚỢỞỠÙÚỤỦŨỪỨỰỬỮỲÝỴỶỸ")


# ---------------------------------------------------------------- text helpers

def norm(s):
    """Lowercase, straight quotes, no markdown emphasis, collapsed whitespace."""
    s = s.replace("“", '"').replace("”", '"').replace("’", "'").replace("‘", "'")
    s = re.sub(r"[*`_]", "", s)
    return re.sub(r"\s+", " ", s).strip().lower()


def strip_md(s):
    return re.sub(r"[*`]", "", s).strip()


def as_list(v):
    return v if isinstance(v, list) else [v]


def flags_of(spec):
    table = {"i": re.I, "m": re.M, "s": re.S}
    out = 0
    for ch in spec:
        out |= table[ch]
    return out


def rx(p, pattern, default="i"):
    return re.compile(pattern, flags_of(p.get("flags", default)))


def clean_title(title):
    t = re.sub(r"[*`]", "", title)
    t = HEAD_NUMBER_RE.sub("", t)  # "3. ", "11.2 " in front of the name
    return t.strip().rstrip(":").strip()


def title_key(title):
    return clean_title(title).lower()


def expand_cant(s):
    """`can't be tested` is `cannot be tested`."""
    return re.sub(r"(?i)\bcan['\u2019]t\b", "cannot", s)


def strip_emphasis(s):
    """`**As a** patient` reads as `As a patient`; list bullets (`* item`) and snake_case stay."""
    s = BOLD_RE.sub(r"\2", s)
    s = ITALIC_STAR_RE.sub(r"\1", s)
    return ITALIC_UNDERSCORE_RE.sub(r"\1", s)


def parse_sections(text):
    """Sections in document order, as dicts. A section starts at a Markdown heading, at a bold
    label with a colon (`**Assumptions**: ...`) or at a line that is only bold. Sections nest:
    a deeper heading, or a bold label inside a heading, does not end the section it sits in
    (`**High**` under `## Gaps` is part of Gaps); a heading of the same or a higher level does.
    A bold label ends the previous bold label but not the heading around it."""
    nodes, stack = [], []

    def open_node(level, title, first):
        while stack and stack[-1]["level"] >= level:
            stack.pop()
        node = {"level": level, "title": clean_title(title), "key": title_key(title), "lines": []}
        if first:
            node["lines"].append(first)
        nodes.append(node)
        return node

    for line in text.splitlines():
        m = HEAD_RE.match(line)
        if m:
            level = len(line.strip()) - len(line.strip().lstrip("#"))
            node = open_node(level, m.group(1), None)
        else:
            m = BOLD_LABEL_RE.match(line)
            if m and title_key(m.group(1)) not in VERDICT_WORDS:
                node = open_node(7, m.group(1), m.group(2) or None)
            else:
                m = BOLD_LINE_RE.match(line) or BOLD_PAREN_RE.match(line)
                if m and title_key(m.group(1)) not in VERDICT_WORDS:
                    node = open_node(7, m.group(1), m.group(2) if m.lastindex == 2 else None)
                else:
                    for n in stack:
                        n["lines"].append(line)
                    continue
        for n in stack:  # the new section's own first line belongs to the sections around it
            n["lines"].append(line)
        stack.append(node)
    return nodes


def split_sections(text):
    """[(key, body)] in document order; a body includes the sections nested inside it."""
    return [(n["key"], "\n".join(n["lines"])) for n in parse_sections(text)]


def name_matches(key, name):
    """`ac` is the section `AC` or `AC: ...`, not `ACC-01 Log in`; a longer title may follow the name."""
    return key == name or (key.startswith(name) and not key[len(name)].isalnum())


def name_variants(names):
    keys = []
    for n in as_list(names):
        keys.append(n.lower())
        keys.extend(SECTION_ALIASES.get(n.lower(), []))
    return keys


def find_sections(text, names):
    """[(position, body)] of the sections with one of these names. The rest of the title after
    the name counts as text of the section (`## Verdict: Not ready`, `## NFRs found (hand off
    to nfr-writer)`). A section inside another matching section is not returned twice."""
    keys = name_variants(names)
    found, covered = [], []
    nodes = parse_sections(text)
    for i, n in enumerate(nodes):
        k = next((k for k in keys if name_matches(n["key"], k)), None)
        if k is None:
            continue
        # nested sections sit after this one in `nodes`; skip them when this one already holds them
        if any(a <= i <= b for a, b in covered):
            continue
        end = i
        for j in range(i + 1, len(nodes)):
            if nodes[j]["level"] > n["level"]:
                end = j
            else:
                break
        covered.append((i, end))
        tail = n["title"][len(k):].lstrip(" :–—-") if len(n["title"]) > len(k) else ""
        found.append((i, "\n".join(([tail] if tail else []) + n["lines"])))
    return found


def get_section(text, names):
    found = find_sections(text, names)
    return "\n".join(b for _, b in found) if found else None


def blocks(text):
    """Table rows, list items and prose lines; indented continuation lines join the item above."""
    out = []
    for line in text.splitlines():
        if not line.strip():
            continue
        if out and re.match(r"^(\s{2,}|\t)\S", line) and not BLOCK_START_RE.match(line.lstrip()[:3] or ""):
            out[-1] += " " + line.strip()
        else:
            out.append(line.strip())
    return out


def split_row(line):
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [strip_md(c) for c in s.split("|")]


def parse_tables(text):
    lines = text.splitlines()
    tables, i = [], 0
    while i < len(lines) - 1:
        if "|" in lines[i] and "|" in lines[i + 1] and SEPARATOR_RE.match(lines[i + 1]):
            headers, rows, j = split_row(lines[i]), [], i + 2
            while j < len(lines) and "|" in lines[j] and lines[j].strip():
                rows.append(split_row(lines[j]))
                j += 1
            tables.append((headers, rows))
            i = j
        else:
            i += 1
    return tables


def column_cells(body, column_re):
    out = []
    for headers, rows in parse_tables(body):
        idx = next((n for n, h in enumerate(headers) if re.search(column_re, h, re.I)), None)
        if idx is None:
            continue
        out.extend(r[idx] for r in rows if idx < len(r))
    return out


def norm_dashes(s):
    return DASHES_RE.sub("-", s)


def find_ids(s):
    return ID_RE.findall(norm_dashes(s))


def example_ids(s, req_prefixes):
    """Codes that the text offers as an example (`such as AES-256`, `e.g. UTF-8`). A code with a
    requirement-style prefix (US, TC, GOAL, ...) is never an example: `for example TC-01` is
    still a made-up test case."""
    s = norm_dashes(s)
    out = set()
    for m in ID_RE.finditer(s):
        if m.group(0).split("-")[0] in req_prefixes:
            continue
        line_start = s.rfind("\n", 0, m.start()) + 1
        if EXAMPLE_MARKER_RE.search(s[max(line_start, m.start() - 80):m.start()]):
            out.add(m.group(0))
    return out


def expand_ranges(s):
    """`US-01 to US-05` also counts as the codes in between."""
    out = set()
    for pre, a, b in RANGE_RE.findall(norm_dashes(s)):
        if int(a) <= int(b) <= int(a) + 200:
            out |= {f"{pre}-{n:0{len(a)}d}" for n in range(int(a), int(b) + 1)}
    return out


def example_data_removed(s):
    """Dates and clock times written as example data inside Given/When/Then are not figures the
    answer made up. A line counts when it has Given, When or Then, or sits under a less indented
    line that has one (the bullets under `- Then:`). The same date or time elsewhere still counts."""
    out, stack = [], []  # stack of (indent, inside Given/When/Then)
    for line in s.splitlines():
        if not line.strip():
            out.append(line)
            continue
        indent = len(line) - len(line.lstrip())
        while stack and stack[-1][0] >= indent:
            stack.pop()
        inside = bool(GWT_RE.search(line)) or bool(stack and stack[-1][1])
        stack.append((indent, inside))
        out.append(EXAMPLE_DATA_RE.sub(" ", line) if inside else line)
    return "\n".join(out)


def clean_for_numbers(s, examples=False):
    s = ISO_DATE_RE.sub(" ", norm_dashes(s))
    if examples:
        s = example_data_removed(s)
    s = ID_RE.sub(" ", s)
    s = REF_NUMBER_RE.sub(" ", s)
    s = LABEL_RE.sub(" ", s)
    s = VARIABLE_RANGE_RE.sub(" ", s)
    s = VARIABLE_STEP_RE.sub(" ", s)
    s = COUNTER_RESET_RE.sub(" ", s)
    s = PERCENTILE_RE.sub(" ", s)
    s = OWN_COUNT_RE.sub(" ", s)
    s = ZERO_PADDED_RE.sub(" ", s)
    s = re.sub(r"https?://\S+", " ", s)
    s = re.sub(r"(?m)^\s*\|\s*\d+\s*\|", "|", s)  # row numbers in the first column of a table
    return re.sub(r"(?m)^\s*(?:#+\s*)?(?:\d+(?:\.\d+)+[.)]?|\d+[.)])\s", " ", s)


def number_keys(s, examples=False):
    keys = {str(float(NUMBER_WORDS[w.lower()])) for w in NUMBER_WORD_RE.findall(s)}
    for n in NUMBER_RE.findall(clean_for_numbers(s, examples)):
        keys.add(str(float(n.replace(",", "."))))
    return keys


def read_fixture(name):
    return (FIXTURES / name).read_text(encoding="utf-8")


class Ctx:
    def __init__(self, case, text, meta=None):
        self.case, self.text, self.meta = case, text, meta or {}
        self.sources = case["prompt"] + "\n" + "\n".join(
            read_fixture(n) for n in case.get("fixtures", []))


def scope(ctx, p):
    """(text to check, error). `section` limits the text; `section_optional` tolerates absence."""
    sec = p.get("section")
    if sec is None:
        return expand_cant(strip_emphasis(ctx.text)), None
    body = get_section(ctx.text, sec)
    if body is None:
        return ("", None) if p.get("section_optional") else (None, f"section {sec} not found")
    return expand_cant(strip_emphasis(body)), None


# ---------------------------------------------------------------------- checks

def chk_sections(ctx, p):
    missing, last, ordered = [], -1, True
    for n in p["names"]:
        found = find_sections(ctx.text, n)
        label = as_list(n)[0]
        if not found:
            missing.append(label)
            continue
        if p.get("non_empty") and not any(re.sub(r"[\W_]+", "", b) and
                                          len(re.sub(r"[\W_]+", "", b)) >= 3 for _, b in found):
            missing.append(f"{label} (empty)")
        if found[0][0] < last:
            ordered = False
        last = max(last, found[0][0])
    if missing:
        return False, "missing: " + ", ".join(missing)
    if p.get("ordered") and not ordered:
        return False, "sections are out of order"
    return True, ""


def chk_match(ctx, p):
    body, err = scope(ctx, p)
    if err:
        return False, err
    n = len(rx(p, p["pattern"]).findall(body))
    lo, hi = p.get("min", 1), p.get("max")
    if n < lo:
        return False, f"/{p['pattern']}/ matched {n} times, need at least {lo}"
    if hi is not None and n > hi:
        return False, f"/{p['pattern']}/ matched {n} times, at most {hi} allowed"
    return True, ""


def sentence_start(body, pos):
    """Start of the sentence that holds `pos`; a full stop inside a code (AC-01.1) does not end it."""
    cut = [m.end() for m in re.finditer(r"[!?\n]|\.\s", body[:pos])]
    return cut[-1] if cut else 0


def item_text(code, sources):
    """Text of the item `code` in the input: every line that holds the code and, for a heading
    (`### US-02 Cancel`), the lines under it up to the next heading."""
    lines, out = sources.splitlines(), []
    for i, line in enumerate(lines):
        if re.search(r"(?<![A-Za-z0-9-])" + re.escape(code) + r"(?![\d])", norm_dashes(line)):
            out.append(line)
            if line.lstrip().startswith("#"):
                for nxt in lines[i + 1:]:
                    if nxt.lstrip().startswith("#"):
                        break
                    out.append(nxt)
    return norm("\n".join(out))


def line_of(body, pos):
    a = body.rfind("\n", 0, pos) + 1
    b = body.find("\n", pos)
    return body[a:b if b >= 0 else len(body)]


def chk_labels(ctx, p):
    """`[Stated]` counts as it is. The short form `[S]` (also `[S/I]`) counts only when the same
    document explains it, e.g. `Labels: [S] stated by you`; the line that explains it is not a use."""
    body, err = scope(ctx, p)
    if err:
        return False, err
    word, short = p["word"], p["short"]
    full = re.compile(r"\[(?:" + "|".join([word] + p.get("also", [])) + r")\b[^\]]*\]")
    n = len(full.findall(body))
    legend = re.compile(r"\[" + short + r"\]\s*[:=\u2013-]?\s*[^\n,;.\[]{0,25}?" + p["legend_word"], re.I)
    tags = [t for t in re.findall(r"\[([SIA](?:/[SIA])*)\]", body) if short in t.split("/")]
    legends = len(legend.findall(body))
    if legends:
        n += max(len(tags) - legends, 0)
    need = p.get("min", 1)
    if n < need:
        why = "" if legends or not tags else f" ([{short}] is used but never explained)"
        return False, f"{n} use(s) of the label {word}, need {need}{why}"
    return True, ""


def chk_not_match(ctx, p):
    body, err = scope(ctx, p)
    if err:
        return False, err
    for m in rx(p, p["pattern"]).finditer(body):
        if p.get("unless_negated"):  # "I cannot tell you it passes" is a refusal, not a claim
            start = max(body.rfind(c, 0, m.start()) for c in ".!?\n") + 1
            if NEGATION_RE.search(body[start:m.start()]):
                continue
        if p.get("unless_sourced_by_code"):  # "US-02 says 2 hours" quotes the item it names
            figure = norm(m.group(0))
            if any(figure in item_text(i, ctx.sources) for i in find_ids(line_of(body, m.start()))):
                continue
        if p.get("unless_line_matches"):  # a refusal that repeats the forbidden words is not a use of them
            if re.search(p["unless_line_matches"], line_of(body, m.start()), re.I):
                continue
        if p.get("unless_about_items"):  # "AC-01.1 passes the checklist" says something about one item
            if find_ids(body[sentence_start(body, m.start()):m.start()]):
                continue
        return False, f"forbidden text found: {m.group(0)[:60]!r}"
    return True, ""


def chk_ids_subset(ctx, p):
    body, err = scope(ctx, p)
    if err:
        return False, err
    allowed = set(find_ids(ctx.sources)) | set(p.get("extra_allowed", []))
    req_prefixes = REQ_PREFIXES | {i.split("-")[0] for i in allowed}
    new = sorted(set(find_ids(body)) - allowed - example_ids(body, req_prefixes))
    if not new:
        return True, ""
    if p.get("new_ids") == "need_marker":
        paras = re.split(r"\n\s*\n", norm_dashes(ctx.text))
        unmarked = [i for i in new if not any(
            re.search(r"(?<![A-Za-z0-9-])" + re.escape(i) + r"(?!\d)", q) and
            re.search(p.get("marker", "proposed"), q, re.I) for q in paras)]
        if not unmarked:
            return True, ""
        new = unmarked
    return False, "codes not in the input" + (" or not marked" if p.get("new_ids") else "") + ": " + ", ".join(new)


def chk_ids_all(ctx, p):
    body, err = scope(ctx, p)
    if err:
        return False, err
    body, ranged = norm_dashes(body), expand_ranges(body)
    missing = [i for i in p["ids"]
               if i not in ranged and not re.search(r"(?<![A-Za-z0-9-])" + re.escape(i) + r"(?!\d)", body)]
    cover = 1 - len(missing) / len(p["ids"])
    if cover + 1e-9 < p.get("min_coverage", 1.0):
        return False, "not mentioned: " + ", ".join(missing)
    return True, ""


def chk_rows(ctx, p):
    """Each expected item needs a block of its own (a row that mentions every code and every
    keyword counts once). `required: true` items must all be found; `min_recall` applies to all."""
    body, err = scope(ctx, p)
    if err:
        return False, err
    bl = blocks(body)

    def hits(anchor, extra=None):
        return [n for n, b in enumerate(bl)
                if all(re.search(a, b, re.I) for a in as_list(anchor)) and
                (extra is None or any(re.search(k, b, re.I) for k in extra))]

    expect = p.get("expect", [])
    options = {e["id"]: hits(e["anchor"], e.get("any") or None) for e in expect}
    owner = {}  # block -> expectation id

    def place(eid, seen):
        for n in options[eid]:
            if n in seen:
                continue
            seen.add(n)
            if n not in owner or place(owner[n], seen):
                owner[n] = eid
                return True
        return False

    # required items first: later augmenting paths never unmatch an item that is already matched
    for e in sorted(expect, key=lambda e: not e.get("required")):
        place(e["id"], set())
    found = set(owner.values())
    missed = [e["id"] for e in expect if e["id"] not in found]
    recall = len(found) / len(expect) if expect else 1.0
    false = [c["id"] for c in p.get("controls", []) if hits(c["anchor"], [c["flag"]])]
    problems = []
    required_missed = [e["id"] for e in expect if e.get("required") and e["id"] not in found]
    if required_missed:
        problems.append("required finding(s) not found: " + ", ".join(required_missed))
    if recall + 1e-9 < p.get("min_recall", 1.0):
        problems.append(f"recall {len(found)}/{len(expect)}, missed: {', '.join(missed)}")
    if len(false) > p.get("max_false", 0):
        problems.append("flagged items that are fine: " + ", ".join(false))
    return (False, "; ".join(problems)) if problems else (True, f"recall {len(found)}/{len(expect)}")


def chk_links(ctx, p):
    """Facts about the fixture's links: each `together` pair of codes must share a row/line of
    the section, no `never` pair may."""
    body, err = scope(ctx, p)
    if err:
        return False, err
    bl = [norm_dashes(b) for b in blocks(body)]

    def shares(a, b):
        return any(re.search(r"(?<![A-Za-z0-9-])" + re.escape(a) + r"(?![\d.]*\d)", x) and
                   re.search(r"(?<![A-Za-z0-9-])" + re.escape(b) + r"(?![\d.]*\d)", x) for x in bl)

    lost = [f"{a}~{b}" for a, b in p.get("together", []) if not shares(a, b)]
    wrong = [f"{a}~{b}" for a, b in p.get("never", []) if shares(a, b)]
    problems = []
    if lost:
        problems.append("links missing: " + ", ".join(lost))
    if wrong:
        problems.append("links that the input does not support: " + ", ".join(wrong))
    return (False, "; ".join(problems)) if problems else (True, "")


def chk_items_resolve(ctx, p):
    body, err = scope(ctx, p)
    if err:
        return False, err
    cells = column_cells(body, p["column"])
    if len(cells) < p.get("min_rows", 1):
        return False, f"only {len(cells)} rows in column /{p['column']}/"
    src_ids, src_norm = set(find_ids(ctx.sources)), norm(ctx.sources)
    bad = []
    for cell in cells:
        ids = set(find_ids(cell))
        quoted = re.findall(r'"([^"]{8,})"|“([^”]{8,})”', cell)
        quotes = [norm(a or b) for a, b in quoted]
        if ids and ids <= src_ids:
            continue
        if ids and not ids <= src_ids:
            bad.append(cell[:50])
        elif quotes and any(q in src_norm for q in quotes):
            continue
        else:
            bad.append(cell[:50])
    return (False, "cannot find in the input: " + " | ".join(bad)) if bad else (True, "")


def chk_numbers(ctx, p):
    body, err = scope(ctx, p)
    if err:
        return False, err
    if p.get("column"):
        body = "\n".join(column_cells(body, p["column"]))
    allowed = number_keys(ctx.sources) | {str(float(a)) for a in p.get("allow", [])}
    invented = sorted(number_keys(body, examples=True) - allowed, key=float)
    return (False, "numbers not in the input: " + ", ".join(invented)) if invented else (True, "")


def chk_no_vague_ac(ctx, p):
    body, err = scope(ctx, p)
    if err:
        return False, err
    words = p.get("words", DEFAULT_VAGUE)
    bad = []
    for b in blocks(body):
        if CONCRETE_AMOUNT_RE.search(re.sub(r"^\s*\d+[.)]\s", "", b)):
            continue
        b = QUOTED_RE.sub(" ", b)  # a quoted message ("Không tìm thấy đơn phù hợp") is wording, not a requirement
        for w in words:
            if re.search(r"(?<!\w)" + re.escape(w) + r"(?!\w)", b, re.I):
                bad.append(f"{w!r} in {b[:50]!r}")
                break
    return (False, "vague word without a criterion: " + "; ".join(bad)) if bad else (True, "")


def chk_story_shape(ctx, p):
    body, err = scope(ctx, p)
    if err:
        return False, err
    bad = []
    for line in body.splitlines():
        m = re.search(r"(?:\bI want|\btôi muốn)\b(.+?)(?=,?\s*(?:so that|để)\b|$)", line, re.I)
        if m and len(re.findall(r"\b(?:and|và)\b|,", m.group(1), re.I)) >= 2:
            bad.append(line.strip()[:60])
    return (False, "two or more 'and' or commas in the want part: " + " | ".join(bad)) if bad else (True, "")


VERDICTS = [("Not ready", r"\bnot ready\b"), ("Conditional", r"\bconditional(?:ly)?\b"),
            ("Ready", r"(?<!not )\bready\b")]


def verdict_of(body):
    best = None
    for name, pat in VERDICTS:
        m = re.search(pat, body, re.I)
        if m and (best is None or m.start() < best[1]):
            best = (name, m.start())
    return best[0] if best else None


def chk_verdict(ctx, p):
    body, err = scope(ctx, {"section": p.get("section", ["Verdict"])})
    if err:
        return False, err
    v = verdict_of(body)
    if v is None:
        return False, "no verdict (Ready / Conditional / Not ready) found"
    if v in p.get("forbid", []):
        return False, f"verdict {v!r} is not acceptable here"
    if p.get("expect") and v != p["expect"]:
        return False, f"verdict {v!r}, expected {p['expect']!r}"
    src = p.get("blockers_from")
    if src:
        fbody = get_section(ctx.text, src["section"]) or ""
        n = sum(1 for c in column_cells(fbody, src.get("column", "level")) if re.match(r"\s*blocker", c, re.I))
        if n and v == "Ready":
            return False, f"verdict Ready although the report lists {n} Blocker finding(s)"
    return True, v


def chk_column_values(ctx, p):
    body, err = scope(ctx, p)
    if err:
        return False, err
    cells = column_cells(body, p["column"])
    if len(cells) < p.get("min_rows", 1):
        return False, f"only {len(cells)} rows in column /{p['column']}/"
    allowed = [a.lower() for a in p["allowed"]]
    bad = [c for c in cells if not any(norm(c).startswith(a) for a in allowed)]
    return (False, "values outside the allowed set: " + ", ".join(bad[:5])) if bad else (True, "")


def chk_table_columns(ctx, p):
    body, err = scope(ctx, p)
    if err:
        return False, err
    for headers, rows in parse_tables(body):
        if all(any(re.search(c, h, re.I) for h in headers) for c in p["columns"]):
            if len(rows) >= p.get("min_rows", 0):
                return True, ""
            return False, f"table has {len(rows)} rows, need {p['min_rows']}"
    return False, "no table with columns: " + ", ".join(p["columns"])


def chk_language(ctx, p):
    letters = [c for c in ctx.text if c.isalpha()]
    ratio = sum(c in VIETNAMESE_CHARS for c in letters) / max(len(letters), 1)
    if p["lang"] == "vi":
        return (True, "") if ratio >= 0.10 else (False, f"does not read as Vietnamese (diacritic ratio {ratio:.3f})")
    return (True, "") if ratio <= 0.02 else (False, f"does not read as English (diacritic ratio {ratio:.3f})")


def chk_verbatim(ctx, p):
    text = norm(ctx.text)
    missing = [ph for ph in p["phrases"] if norm(ph) not in text]
    return (False, "wording not kept: " + " | ".join(missing)) if missing else (True, "")


def chk_distinct_terms(ctx, p):
    body, err = scope(ctx, p)
    if err:
        return False, err
    found = [t for t in p["terms"] if re.search(r"\b" + re.escape(t) + r"\b", body, re.I)]
    if len(found) < p["min"]:
        return False, f"{len(found)} of {len(p['terms'])} terms named, need {p['min']}"
    return True, ""


def chk_link_requires_marker(ctx, p):
    marker = re.compile(p["marker"], re.I)
    linked = [b for b in blocks(ctx.text) if all(re.search(a, b, re.I) for a in p["anchor"])
              and not b.rstrip().endswith("?")]  # a question to confirm is not a stated link
    bad = [b[:60] for b in linked if not marker.search(b)]
    return (False, "link stated without a basis marker: " + " | ".join(bad)) if bad else (True, "")


def chk_any_of(ctx, p):
    details = []
    for sub in p["checks"]:
        ok, detail = run_check(ctx, sub)
        if ok:
            return True, ""
        details.append(detail)
    return False, "none of the alternatives passed: " + " / ".join(details)


def chk_no_missing_resource(ctx, p):
    install = set(ctx.case["install"])
    others = sorted({d.name for d in SKILLS.iterdir() if d.is_dir()} - install)
    problems = []
    for token in sorted(set(PATH_TOKEN_RE.findall(ctx.text))):
        parts = token.split("/")
        if parts[0] in ("references", "templates", "scripts"):
            if not any((SKILLS / s / token).exists() for s in install):
                problems.append(f"{token} does not exist in the installed skill(s)")
        elif parts[0] not in install:
            problems.append(f"{token} points into a skill that is not installed")
        elif not (SKILLS / token.split("/", 1)[0] / token.split("/", 1)[1]).exists():
            problems.append(f"{token} does not exist")
    for sentence in re.split(r"(?<=[.!?])\s+|\n", ctx.text):
        if LOOKUP_FAILURE_RE.search(sentence):
            for name in others:
                if re.search(r"(?<![\w-])" + re.escape(name) + r"(?![\w-])", sentence):
                    problems.append(f"tried to use {name}: {sentence.strip()[:60]!r}")
    return (False, "; ".join(problems)) if problems else (True, "")


CHECKS = {
    "sections": chk_sections, "match": chk_match, "not_match": chk_not_match,
    "ids_subset": chk_ids_subset, "ids_all": chk_ids_all, "rows": chk_rows,
    "items_resolve": chk_items_resolve, "numbers_from_input": chk_numbers,
    "no_vague_ac": chk_no_vague_ac, "story_shape": chk_story_shape, "verdict": chk_verdict,
    "column_values": chk_column_values, "table_columns": chk_table_columns,
    "language": chk_language, "verbatim": chk_verbatim, "distinct_terms": chk_distinct_terms,
    "link_requires_marker": chk_link_requires_marker, "any_of": chk_any_of,
    "no_missing_resource": chk_no_missing_resource, "links": chk_links, "labels": chk_labels,
}


def run_check(ctx, check):
    try:
        return CHECKS[check["type"]](ctx, check)
    except Exception as e:  # a malformed check must fail loudly, not pass
        return False, f"check crashed: {type(e).__name__}: {e}"


# ----------------------------------------------------------------------- cases

def load_cases(cases_dir=None):
    cases = {}
    for path in sorted((cases_dir or CASES).glob("*/*.yml")):
        case = yaml.safe_load(path.read_text(encoding="utf-8"))
        case["_path"] = path
        if case.get("id") in cases:
            raise ValueError(f"duplicate case id {case['id']}")
        cases[case.get("id", path.stem)] = case
    return cases


def _regex_problems(where, p):
    out = []
    for key in ("pattern", "marker", "column", "flag", "unless_line_matches", "legend_word"):
        if key in p:
            try:
                re.compile(p[key])
            except re.error as e:
                out.append(f"{where}: bad regex in {key}: {e}")
    for key in ("columns", "anchor", "any"):
        for pat in as_list(p.get(key, [])):
            try:
                re.compile(pat)
            except re.error as e:
                out.append(f"{where}: bad regex in {key}: {e}")
    for e in p.get("expect", []) + p.get("controls", []):
        out.extend(_regex_problems(where + "/" + e.get("id", "?"), e))
    for sub in p.get("checks", []):
        out.extend(_regex_problems(where + "/" + sub.get("type", "?"), sub))
    return out


def validate_case(case):
    errs, cid = [], case.get("id", "?")
    for key in ("id", "skill", "kind", "prompt", "checks", "rubric", "bad_expected_failures"):
        if key not in case:
            errs.append(f"{cid}: missing key {key}")
    if errs:
        return errs
    path = case.get("_path")
    if path and (path.stem != cid or path.parent.name != case["skill"]):
        errs.append(f"{cid}: file must be cases/{case['skill']}/{cid}.yml")
    if not (SKILLS / case["skill"]).is_dir():
        errs.append(f"{cid}: unknown skill {case['skill']}")
    if case["kind"] not in KINDS:
        errs.append(f"{cid}: kind must be one of {sorted(KINDS)}")
    if case["kind"] == "standalone":
        install = case.get("install")
        if not install or case["skill"] not in install or any(not (SKILLS / s).is_dir() for s in install):
            errs.append(f"{cid}: standalone case needs `install` listing existing skills, including {case['skill']}")
    for name in case.get("fixtures", []):
        if not (FIXTURES / name).is_file():
            errs.append(f"{cid}: fixture {name} not found")
    if errs:
        return errs
    ids = [c.get("id") for c in case["checks"]]
    if len(set(ids)) != len(ids) or None in ids:
        errs.append(f"{cid}: check ids must be present and unique")
    sources = Ctx(case, "").sources
    for c in case["checks"]:
        where = f"{cid}/{c.get('id')}"
        if c.get("type") not in CHECKS:
            errs.append(f"{where}: unknown check type {c.get('type')}")
            continue
        errs.extend(_regex_problems(where, c))
        for ph in c.get("phrases", []):
            if norm(ph) not in norm(sources):
                errs.append(f"{where}: phrase not in the input: {ph[:40]!r}")
        for i in c.get("ids", []):
            if i not in sources:
                errs.append(f"{where}: id {i} not in the input")
    unknown = set(case["bad_expected_failures"]) - set(ids)
    if unknown:
        errs.append(f"{cid}: bad_expected_failures names unknown checks {sorted(unknown)}")
    if not case["bad_expected_failures"]:
        errs.append(f"{cid}: bad_expected_failures is empty")
    return errs


def build_prompt(case):
    parts = [case["prompt"].rstrip()]
    for name in case.get("fixtures", []):
        parts.append(f"--- {name} ---\n{read_fixture(name).rstrip()}\n--- end of {name} ---")
    return "\n\n".join(parts) + "\n"


def isolation_status(case, meta):
    """(status, detail) for standalone cases; None otherwise. The grader never assumes that a
    temporary folder means a single skill was loaded: it needs the runner's record, and the
    record must show that the skill under test was loaded and no other suite skill was."""
    if case["kind"] != "standalone":
        return None, ""
    loaded = (meta or {}).get("loaded_skills") if isinstance(meta, dict) else None
    if not isinstance(loaded, list) or not all(isinstance(x, str) for x in loaded):
        return "unverified", f"no usable record of loaded skills; cannot tell that only {case['install']} was loaded"
    suite = {d.name for d in SKILLS.iterdir() if d.is_dir()}
    absent = sorted(set(case["install"]) - set(loaded))
    if absent:
        return "violated", "the skill under test was not loaded: " + ", ".join(absent)
    extra = sorted((set(loaded) & suite) - set(case["install"]))
    if extra:
        return "violated", "other suite skills were loaded: " + ", ".join(extra)
    return "verified", ""


def grade_case(case, text, meta=None):
    ctx = Ctx(case, text, meta)
    results = []
    for c in case["checks"]:
        ok, detail = run_check(ctx, c)
        results.append({"id": c["id"], "type": c["type"], "ok": ok, "detail": detail})
    iso, iso_detail = isolation_status(case, meta)
    failed = [r["id"] for r in results if not r["ok"]]
    if iso == "violated":
        status = "fail"
    elif failed:
        status = "fail"
    elif iso == "unverified":
        status = "unverified"
    else:
        status = "pass"
    return {"id": case["id"], "skill": case["skill"], "kind": case["kind"], "status": status,
            "failed": failed, "isolation": iso, "isolation_detail": iso_detail,
            "checks": results, "manual_rubric": case["rubric"]}


# ------------------------------------------------------------------------- CLI

def cmd_list(args):
    cases = load_cases()
    bad = [e for c in cases.values() for e in validate_case(c)]
    for c in cases.values():
        print(f"{c['id']:24} {c['skill']:24} {c['kind']:10} {len(c['checks']):2} checks  rubric {','.join(c['rubric'])}")
    for e in bad:
        print("ERROR", e)
    print(f"{len(cases)} cases, {len(bad)} problems")
    return 1 if bad else 0


def cmd_prompt(args):
    cases = load_cases()
    if args.case not in cases:
        sys.exit(f"unknown case {args.case}")
    sys.stdout.write(build_prompt(cases[args.case]))
    return 0


def cmd_grade(args):
    out = Path(args.outdir)
    cases = load_cases()
    results, missing = [], []
    for cid, case in cases.items():
        f = out / f"{cid}.md"
        if not f.is_file():
            missing.append(cid)
            continue
        meta_f = out / f"{cid}.meta.json"
        try:
            meta = json.loads(meta_f.read_text(encoding="utf-8")) if meta_f.is_file() else None
        except ValueError:
            meta = {"unreadable": True}
        results.append(grade_case(case, f.read_text(encoding="utf-8"), meta))
    for r in results:
        print(f"{r['status'].upper():10} {r['id']}" + (f"  failed: {', '.join(r['failed'])}" if r["failed"] else "")
              + (f"  [{r['isolation_detail']}]" if r["isolation_detail"] else ""))
        for c in r["checks"]:
            if not c["ok"]:
                print(f"           - {c['id']}: {c['detail']}")
    for cid in missing:
        print(f"MISSING    {cid}  (no output file)")
    count = {s: sum(r["status"] == s for r in results) for s in ("pass", "fail", "unverified")}
    print(f"{count['pass']} pass, {count['fail']} fail, {count['unverified']} unverified isolation, {len(missing)} missing")
    (out / "automatic.json").write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    manual = out / "manual.json"
    if not manual.exists():
        sheet = {r["id"]: {rid: None for rid in r["manual_rubric"]} for r in results}
        manual.write_text(json.dumps(sheet, indent=2), encoding="utf-8")
        print(f"created {manual} (scores 0/1 per evals/RUBRIC.md, filled in by hand)")
    # Exit code, by priority: 1 a check failed; 3 an output is missing; 2 nothing failed but isolation
    # is unverified; 0 only when all 17 cases were graded and passed. "unverified" and a partial run
    # are never reported as a pass. --allow-missing is for grading a subset by hand: missing is ignored.
    if count["fail"]:
        return 1
    if missing and not args.allow_missing:
        return 3
    return 2 if count["unverified"] else 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list").set_defaults(fn=cmd_list)
    sp = sub.add_parser("prompt")
    sp.add_argument("case")
    sp.set_defaults(fn=cmd_prompt)
    sg = sub.add_parser("grade")
    sg.add_argument("outdir")
    sg.add_argument("--allow-missing", action="store_true",
                    help="grade a subset: missing outputs are listed but do not change the exit code")
    sg.set_defaults(fn=cmd_grade)
    args = ap.parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
