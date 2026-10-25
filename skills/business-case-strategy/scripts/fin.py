#!/usr/bin/env python3
"""Compute ROI, NPV, IRR and payback period from a year-by-year benefit and cost table.

Usage: python3 fin.py input.json
input.json: {"discount_rate": 0.10, "years": [{"year":0,"benefits":0,"costs":100}, ...]}
Every figure is supplied by the user; the script never generates numbers. Formulas follow BABOK v3
section 10.20.4.5 (ROI, present value, NPV, IRR); the payback period has no standard formula
(BABOK says so explicitly), so it is linearly interpolated here.
"""
import json, sys


def npv(rate, nets):
    return sum(n / (1 + rate) ** t for t, n in enumerate(nets))


def irr(nets, lo=-0.99, hi=10.0, tol=1e-9):
    f = lambda r: npv(r, nets)
    flo, fhi = f(lo), f(hi)
    if flo * fhi > 0:
        return None  # no root in the interval, or the cash flow never changes sign
    for _ in range(300):
        mid = (lo + hi) / 2
        fm = f(mid)
        if abs(fm) < tol:
            return mid
        if flo * fm < 0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return (lo + hi) / 2


def main(path):
    d = json.load(open(path, encoding="utf-8"))
    rate = float(d["discount_rate"])
    rows = sorted(d["years"], key=lambda r: r["year"])
    years = [r["year"] for r in rows]
    if years != list(range(years[0], years[0] + len(years))):
        sys.exit("Years must be consecutive, for example 0,1,2,3.")
    ben = [float(r.get("benefits", 0)) for r in rows]
    cost = [float(r.get("costs", 0)) for r in rows]
    net = [b - c for b, c in zip(ben, cost)]
    cum, run = [], 0.0
    for n in net:
        run += n
        cum.append(run)
    total_b, total_c = sum(ben), sum(cost)
    out = {
        "net_by_year": dict(zip(years, net)),
        "cumulative_net": dict(zip(years, cum)),
        "total_benefits": total_b,
        "total_costs": total_c,
        "roi": (total_b - total_c) / total_c if total_c else None,
        "discount_rate": rate,
        "npv": npv(rate, net),
        "irr": irr(net),
    }
    pb = None
    for i, c in enumerate(cum):
        if c >= 0:
            if i == 0:
                pb = float(years[0])
            else:
                prev = cum[i - 1]
                pb = years[i - 1] + (-prev) / (c - prev)
            break
    out["payback_year"] = pb
    # simple sensitivity: NPV at a few discount rates around the chosen one
    out["npv_sensitivity"] = {f"{r:.2%}": npv(r, net) for r in (rate - 0.05, rate, rate + 0.05) if r > -0.99}
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
