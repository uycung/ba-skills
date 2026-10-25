#!/usr/bin/env python3
"""Live runner for the skill evals: one `claude -p` per case, then the offline grader.

  python3 evals/run.py explicit OUTDIR     "Use the <skill> skill for this task." before the prompt
  python3 evals/run.py natural  OUTDIR     the prompt as written; only measures routing

Each case runs in its own temporary folder with the skills copied to <tmp>/.claude/skills/ (a
standalone case gets only the skills in its `install`, every other case gets all of them), with
--setting-sources project so that personal settings are not read. Per case it writes
OUTDIR/<id>.md (the reply), <id>.jsonl (the raw stream) and <id>.meta.json (skills loaded, skills
invoked, model, cost, turns, error), appends a line to OUTDIR/run.log, and at the end grades the
folder with grade.py (exit code as `grade.py grade`).

Spend is capped per case (--max-budget-usd) and in total; the run stops when the total is used
up or after two runner errors in a row. A case whose output already exists without an error is
skipped, so an interrupted run can be repeated (--force runs it again).
Needs the `claude` CLI, logged in, and PyYAML.
"""
import argparse
import json
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import grade  # noqa: E402

MODES = ("explicit", "natural")
DENIED_TOOLS = ["Bash", "Write", "Edit", "WebFetch", "WebSearch", "Agent"]
ALLOWED_TOOLS = ["Read", "Skill"]


def prompt_for(case, mode):
    text = grade.build_prompt(case)
    if mode == "explicit":
        return f"Use the {case['skill']} skill for this task.\n\n{text}"
    return text


def skills_for(case):
    if case["kind"] == "standalone":
        return list(case["install"])
    return sorted(d.name for d in grade.SKILLS.iterdir() if d.is_dir())


def command(model, budget):
    return ["claude", "-p", "--setting-sources", "project", "--model", model,
            "--output-format", "stream-json", "--verbose", "--max-budget-usd", f"{budget:.2f}",
            "--allowedTools", ",".join(ALLOWED_TOOLS), "--disallowedTools", ",".join(DENIED_TOOLS),
            "--no-session-persistence"]


def parse_stream(raw):
    """(reply text, meta fields) from the stream-json lines of one run."""
    loaded, invoked, files_read, last_text, result = [], [], [], "", None
    model = None
    for line in raw.splitlines():
        try:
            ev = json.loads(line)
        except ValueError:
            continue
        kind = ev.get("type")
        if kind == "system" and ev.get("subtype") == "init":
            loaded = list(ev.get("skills") or [])
            model = ev.get("model")
        elif kind == "assistant":
            texts = []
            for block in (ev.get("message") or {}).get("content") or []:
                if block.get("type") == "tool_use" and block.get("name") == "Skill":
                    name = (block.get("input") or {}).get("skill")
                    if name and name not in invoked:
                        invoked.append(name)
                elif block.get("type") == "tool_use" and block.get("name") == "Read":
                    path = (block.get("input") or {}).get("file_path")
                    if path:
                        files_read.append(path)
                elif block.get("type") == "text":
                    texts.append(block.get("text", ""))
            if texts:
                last_text = "\n".join(texts)
        elif kind == "result":
            result = ev
    text = (result or {}).get("result") or last_text
    return text, {"loaded_skills": loaded, "skill_invoked": invoked, "model": model,
                  "files_read": files_read}, result


def run_case(case, mode, out, model, budget, timeout, keep):
    tmp = Path(tempfile.mkdtemp(prefix=f"eval-{case['id']}-"))
    try:
        for name in skills_for(case):
            shutil.copytree(grade.SKILLS / name, tmp / ".claude" / "skills" / name)
        started, error, raw = time.time(), None, ""
        try:
            proc = subprocess.run(command(model, budget), input=prompt_for(case, mode), cwd=tmp, text=True,
                                  capture_output=True, timeout=timeout)
            raw = proc.stdout
            if proc.returncode != 0 and not raw.strip():
                error = f"claude exited {proc.returncode}: {proc.stderr.strip()[:300]}"
        except subprocess.TimeoutExpired as e:
            raw = (e.stdout.decode() if isinstance(e.stdout, bytes) else e.stdout) or ""
            error = f"timeout after {timeout}s"
        text, meta, result = parse_stream(raw)
        if error is None:
            if result is None:
                error = "no result event in the stream"
            elif result.get("is_error") or result.get("subtype") != "success":
                error = f"{result.get('subtype')}: {str(result.get('result') or result.get('errors'))[:300]}"
            elif not text.strip():
                error = "empty reply"
        meta.update({"model_requested": model, "cost_usd": (result or {}).get("total_cost_usd") or 0.0,
                     "turns": (result or {}).get("num_turns"), "error": error, "mode": mode,
                     "seconds": round(time.time() - started),
                     "permission_denials": len((result or {}).get("permission_denials") or [])})
        (out / f"{case['id']}.jsonl").write_text(raw, encoding="utf-8")
        (out / f"{case['id']}.md").write_text(text, encoding="utf-8")
        (out / f"{case['id']}.meta.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
        return meta
    finally:
        if not keep:
            shutil.rmtree(tmp, ignore_errors=True)


def already_done(out, cid):
    meta, md = out / f"{cid}.meta.json", out / f"{cid}.md"
    try:
        return md.is_file() and json.loads(meta.read_text(encoding="utf-8")).get("error") is None
    except (OSError, ValueError):
        return False


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mode", choices=MODES)
    ap.add_argument("outdir")
    ap.add_argument("--cases", help="comma-separated case ids (default: all)")
    ap.add_argument("--model", default="claude-sonnet-5-5")
    ap.add_argument("--case-budget", type=float, default=1.5, help="USD cap for one case")
    ap.add_argument("--total-budget", type=float, default=8.0, help="USD cap for the whole run")
    ap.add_argument("--max-runner-errors", type=int, default=2, help="stop after this many errors in a row")
    ap.add_argument("--timeout", type=int, default=900, help="seconds per case")
    ap.add_argument("--force", action="store_true", help="run cases that already have an output")
    ap.add_argument("--keep-tmp", action="store_true", help="keep the temporary folders")
    ap.add_argument("--no-grade", action="store_true")
    args = ap.parse_args(argv)

    cases = grade.load_cases()
    ids = args.cases.split(",") if args.cases else list(cases)
    unknown = [i for i in ids if i not in cases]
    if unknown:
        sys.exit("unknown case(s): " + ", ".join(unknown))
    out = Path(args.outdir)
    out.mkdir(parents=True, exist_ok=True)

    spent, streak, stopped = 0.0, 0, None
    for cid in ids:
        if not args.force and already_done(out, cid):
            print(f"{cid:24} skipped (output exists)")
            continue
        remaining = args.total_budget - spent
        if remaining <= 0.01:
            stopped = f"total budget ${args.total_budget:.2f} used up"
            break
        meta = run_case(cases[cid], args.mode, out, args.model, min(args.case_budget, remaining),
                        args.timeout, args.keep_tmp)
        spent += meta["cost_usd"]
        line = (f"{cid:24} cost=${meta['cost_usd']:.3f} turns={meta['turns']} invoked={meta['skill_invoked']} "
                f"err={meta['error']} total=${spent:.2f}")
        print(line, flush=True)
        with (out / "run.log").open("a", encoding="utf-8") as f:
            f.write(line + "\n")
        streak = streak + 1 if meta["error"] else 0
        if streak >= args.max_runner_errors:
            stopped = f"{streak} runner errors in a row"
            break
    if stopped:
        print("STOPPED:", stopped)
    print(f"spent ${spent:.2f}")
    if args.no_grade:
        return 0
    return grade.main(["grade", str(out), "--allow-missing"])


if __name__ == "__main__":
    sys.exit(main())
