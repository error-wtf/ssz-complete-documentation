#!/usr/bin/env python3
"""
run_full_pipeline.py
====================
Documentation pipeline for the SSZ complete-documentation repository.

This repository is pure documentation (Markdown only, no test code), so the
"full pipeline" is a documentation-integrity pipeline:

  (a) INVENTORY      -- count Markdown files per section directory
                        (00_INDEX ... 13_FREQUENCY_FRAMEWORK) and repo-wide.
  (b) LINK CHECK     -- resolve every relative Markdown link in every .md
                        file; report dead targets (missing files). Anchors
                        (`#...`) are counted but not verified (no reliable
                        slug algorithm); external http(s) links are listed
                        separately (not fetched -- offline repo check).
  (c) FORMULA CHECK  -- verify the canonical key numbers of the framework
                        (02_FOUNDATIONS/, 03_FORMULAS/) for arithmetic
                        consistency and cross-file presence:
                          Xi(r_s)        = 0.80171   (= 1 - e^(-phi))
                          D(r_s)         = 0.55503   (= 1/(1+Xi(r_s)))
                          r*/r_s global  = 1.594811  (D_SSZ = D_GR, decay)
                          r*/r_s local   = 1.386562  (saturation form)
                        plus secondary documented identities
                        (1-1/e = 0.63212, D_SSZ(phi*r_s) = 0.61270,
                        D_GR(phi*r_s) = 1/phi = 0.618034, phi = 1.618034).

The pipeline NEVER modifies repository files. It only writes the report
`FULL_PIPELINE_REPORT.md` into the repository root (dead links are listed,
not silently fixed).

Sources for all checked numbers (single source of truth):
  03_FORMULAS/special_values.md, 03_FORMULAS/formula_compendium.md,
  02_FOUNDATIONS/time_dilation.md, 02_FOUNDATIONS/segment_density.md,
  02_FOUNDATIONS/regime_definitions.md,
  02_FOUNDATIONS/phi_lattice_discretization.md  (all read before coding).

Run:  /home/error/physics/venv/bin/python tools/run_full_pipeline.py
(requires only the Python standard library)

Documentation copyright: (c) 2025-2026 Carmen N. Wrede, Lino P. Casu
"""

from __future__ import annotations

import datetime as _dt
import math
import os
import re
import sys
from collections import defaultdict

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECTIONS = [
    "00_INDEX", "01_OVERVIEW", "02_FOUNDATIONS", "03_FORMULAS",
    "04_KINEMATICS", "05_ELECTROMAGNETISM", "06_STRONG_FIELD",
    "07_VALIDATION", "08_FALSIFICATION", "09_PAPERS", "10_REPOSITORIES",
    "11_GUARDRAILS", "12_GLOSSARY", "13_FREQUENCY_FRAMEWORK",
]

# Canonical key numbers (special_values.md / formula_compendium.md)
KEY_NUMBERS = {
    "Xi(r_s) = 0.80171": "0.55503-partner",
    "D(r_s) = 0.55503": "0.55503",
    "r*/r_s decay/global = 1.594811": "1.594811",
    "r*/r_s saturation/local = 1.386562": "1.386562",
}
KEY_STRING_NUMBERS = ["0.55503", "0.80171", "1.594811", "1.386562"]

# Files where the key numbers are canonically documented (subset checked hard)
CANONICAL_CARRIERS = [
    "02_FOUNDATIONS/time_dilation.md",
    "02_FOUNDATIONS/segment_density.md",
    "02_FOUNDATIONS/phi_lattice_discretization.md",
    "03_FORMULAS/special_values.md",
    "03_FORMULAS/formula_compendium.md",
    "README.md",
]

MD_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
TOL = 5e-6


# ---------------------------------------------------------------------------
def iter_md_files():
    for dirpath, dirnames, filenames in os.walk(REPO_ROOT):
        dirnames[:] = [d for d in sorted(dirnames)
                       if not d.startswith(".") and d not in ("output", "__pycache__")]
        for fn in sorted(filenames):
            if fn.lower().endswith(".md"):
                # exclude this pipeline's own generated report (self-reference)
                if os.path.abspath(os.path.join(dirpath, fn)) == os.path.join(REPO_ROOT, "FULL_PIPELINE_REPORT.md"):
                    continue
                yield os.path.join(dirpath, fn)


def step_inventory():
    """(a) Markdown inventory per section + repo-wide."""
    counts = {}
    for sec in SECTIONS:
        p = os.path.join(REPO_ROOT, sec)
        counts[sec] = len([f for f in os.listdir(p)
                           if f.lower().endswith(".md")]) if os.path.isdir(p) else -1
    all_md = [os.path.relpath(f, REPO_ROOT) for f in iter_md_files()]
    root_md = [f for f in all_md if os.sep not in f]
    papers_mirror = [f for f in all_md if f.startswith("09_PAPERS" + os.sep)]
    papers_index = [f for f in papers_mirror
                    if os.sep not in f[len("09_PAPERS") + 1:]]
    return {
        "per_section": counts,
        "total": len(all_md),
        "root_files": root_md,
        "core_total": len(all_md) - len(papers_mirror),
        "papers_mirror_total": len(papers_mirror),
        "papers_index_total": len(papers_index),
        "all": all_md,
    }


def step_linkcheck(all_md):
    """(b) Resolve every relative Markdown link; collect dead targets."""
    dead, external, anchor_only = [], [], 0
    total_links = 0
    for rel in all_md:
        path = os.path.join(REPO_ROOT, rel)
        try:
            text = open(path, encoding="utf-8", errors="replace").read()
        except OSError as e:
            dead.append((rel, f"<unreadable: {e}>"))
            continue
        base = os.path.dirname(path)
        for m in MD_LINK_RE.finditer(text):
            target = m.group(1).strip()
            total_links += 1
            if target.startswith(("http://", "https://", "mailto:")):
                external.append((rel, target))
                continue
            if target.startswith("#"):
                anchor_only += 1
                continue
            file_part = target.split("#", 1)[0]
            if not file_part:
                anchor_only += 1
                continue
            resolved = os.path.normpath(os.path.join(base, file_part))
            if not os.path.exists(resolved):
                dead.append((rel, target))
    dead.sort()
    return {
        "total_links": total_links,
        "dead": dead,
        "dead_count": len(dead),
        "external_count": len(external),
        "external": sorted(set(external)),
        "anchor_only": anchor_only,
    }


def step_formulacheck(all_md):
    """(c) Arithmetic identities + cross-file presence of key numbers."""
    phi = (1 + math.sqrt(5)) / 2
    identities = []

    def chk(name, got, want, tol=TOL):
        ok = abs(got - want) <= tol
        identities.append((name, got, want, "OK" if ok else "MISMATCH"))
        return ok

    xi_rs = 1 - math.exp(-phi)
    chk("Xi(r_s) = 1 - e^(-phi)", xi_rs, 0.80171, 1e-5)
    chk("D(r_s) = 1/(1+0.80171)", 1 / 1.80171, 0.55503, 1e-5)
    chk("z(r_s) = Xi(r_s) (z=0.802 not infinite)", xi_rs, 0.80171, 1e-5)
    chk("phi = 1.618034", phi, 1.618034, 1e-6)
    chk("Xi_decay(phi*r_s) = 1 - 1/e", 1 - 1 / math.e, 0.63212, 1e-5)
    chk("D_SSZ(phi*r_s) = 1/(1+0.63212)", 1 / 1.63212, 0.61270, 1e-5)
    chk("D_GR(phi*r_s) = 1/phi", math.sqrt(1 - 1 / phi), 1 / phi, 1e-12)
    # r* intersections: D_SSZ(x) = D_GR(x) solved from documented branches
    def d_gr(x):
        return math.sqrt(1 - 1 / x)
    def xi_strong(x):
        return 1 - math.exp(-phi / x)
    def xi_weak(x):
        return 1 / (2 * x)
    def f_global(x):  # decay/global comparison branch
        return 1 / (1 + xi_strong(x)) - d_gr(x)
    lo, hi = 1.0, phi  # bracket theorem interval
    for _ in range(200):
        mid = (lo + hi) / 2
        if f_global(lo) * f_global(mid) <= 0:
            hi = mid
        else:
            lo = mid
    chk("r* decay/global (bisection of D_SSZ=D_GR)", (lo + hi) / 2, 1.594811, 1e-5)

    def f_sat(x):  # saturation/local branch: Xi_B(x) = 1 - exp(-phi*x)
        return 1 / (2 - math.exp(-phi * x)) - d_gr(x)
    lo, hi = 1.0, 1.6
    for _ in range(200):
        mid = (lo + hi) / 2
        if f_sat(lo) * f_sat(mid) <= 0:
            hi = mid
        else:
            lo = mid
    x_sat = (lo + hi) / 2
    chk("r* saturation/local (Xi_B=1-exp(-phi*x))", x_sat, 1.386562, 1e-5)
    chk("D(r*) saturation (documented 0.528007)", 1 / (2 - math.exp(-phi * x_sat)), 0.528007, 1e-5)
    chk("z(r*) saturation (documented 0.893914)", 2 - math.exp(-phi * x_sat) - 1, 0.893914, 1e-5)

    # presence of the four key numbers across all .md files
    presence = {}
    for num in KEY_STRING_NUMBERS:
        presence[num] = sorted(
            rel for rel in all_md
            if num in open(os.path.join(REPO_ROOT, rel), encoding="utf-8",
                           errors="replace").read())
    # canonical carriers must contain all four
    carrier_gaps = []
    for carrier in CANONICAL_CARRIERS:
        text = open(os.path.join(REPO_ROOT, carrier), encoding="utf-8",
                    errors="replace").read()
        missing = [n for n in KEY_STRING_NUMBERS if n not in text]
        if missing:
            carrier_gaps.append((carrier, missing))
    # rounded variants (INFO only -- may be legitimate rounding in tables)
    variant_re = re.compile(r"\b(0\.5550(?!3)|0\.8017(?!1)|1\.59481(?!1)|1\.38656(?!2))\b")
    variants = defaultdict(set)
    for rel in all_md:
        text = open(os.path.join(REPO_ROOT, rel), encoding="utf-8",
                    errors="replace").read()
        for m in variant_re.finditer(text):
            variants[m.group(1)].add(rel)
    variants = {k: sorted(v) for k, v in variants.items()}
    return {
        "identities": identities,
        "all_ok": all(i[3] == "OK" for i in identities),
        "presence": presence,
        "carrier_gaps": carrier_gaps,
        "rounded_variants": dict(variants),
    }


def write_report(inv, links, fx, runtime_utc):
    lines = []
    w = lines.append
    w("# Full Pipeline Report — ssz-complete-documentation")
    w("")
    w(f"**Generated (UTC):** {runtime_utc}  ")
    w("**Tool:** `tools/run_full_pipeline.py` (stdlib only — inventory, link check, formula check)  ")
    w("**Mode:** read-only on repository content; this report is the only file written.")
    w("")
    w("---")
    w("")
    w("## 1. Inventory (Markdown files per section)")
    w("")
    w("| Section | .md files |")
    w("|---|---|")
    for sec in SECTIONS:
        n = inv["per_section"][sec]
        w(f"| `{sec}/` | {n if n >= 0 else 'MISSING'} |")
    w(f"| **root (readme, memory, license …)** | {len(inv['root_files'])} |")
    w("")
    w(f"- **Core documentation files (excl. `09_PAPERS/`):** {inv['core_total']}")
    w(f"- **Files under `09_PAPERS/`:** {inv['papers_mirror_total']} "
      f"({inv['papers_index_total']} section indexes + "
      f"{inv['papers_mirror_total'] - inv['papers_index_total']} mirrored paper markdown files in `09_PAPERS/markdown/`; "
      "original PDFs in `09_PAPERS/pdf/` are not counted)")
    w(f"- **Total `.md` files in repository:** {inv['total']}")
    w(f"- Root-level files: {', '.join(f'`{f}`' for f in inv['root_files'])}")
    w("")
    w("> Note: earlier README wording said \"63+ MD files\" — the actual count is "
      f"{inv['core_total']} core files ({inv['total']} including the paper mirror). "
      "README has been corrected in this revision.")
    w("")
    w("## 2. Link Check (relative Markdown links)")
    w("")
    w(f"- Total Markdown links parsed: **{links['total_links']}**")
    w(f"- External (`http(s)://`, `mailto:`) links: **{links['external_count']}** "
      "(listed in appendix, not fetched — offline check)")
    w(f"- Same-file anchor links (`#…`): **{links['anchor_only']}** (not verified — "
      "no reliable GitHub-slug algorithm implemented)")
    w(f"- **Dead relative links (target file missing): {links['dead_count']}**")
    w("")
    if links["dead_count"]:
        w("| # | Source file | Dead target |")
        w("|---|---|---|")
        for i, (src, tgt) in enumerate(links["dead"], 1):
            w(f"| {i} | `{src}` | `{tgt}` |")
        w("")
        w("> Policy: dead links are **reported only** — not silently fixed "
          "(typo fixes allowed only in newly created files).")
        w("")
    else:
        w("**No dead relative links found.** All relative link targets resolve.")
        w("")
    w("## 3. Formula Consistency Check (canonical key numbers)")
    w("")
    w("### 3.1 Arithmetic identities (recomputed with stdlib `math`)")
    w("")
    w("| Identity | Computed | Documented | Status |")
    w("|---|---|---|---|")
    for name, got, want, st in fx["identities"]:
        w(f"| {name} | {got:.6f} | {want} | {st} |")
    w("")
    w(f"**Overall: {'ALL OK' if fx['all_ok'] else 'MISMATCHES FOUND — see table'}**")
    w("")
    w("### 3.2 Cross-file presence of key numbers")
    w("")
    for num in KEY_STRING_NUMBERS:
        w(f"- `{num}` — present in **{len(fx['presence'][num])}** files")
    w("")
    if fx["carrier_gaps"]:
        w("**Canonical carrier gaps (expected files missing a key number):**")
        for carrier, missing in fx["carrier_gaps"]:
            w(f"- `{carrier}` missing: {', '.join(missing)}")
        w("")
    else:
        w("All canonical carrier files "
          f"({', '.join('`%s`' % c for c in CANONICAL_CARRIERS)}) contain all four key numbers.")
        w("")
    if fx["rounded_variants"]:
        w("### 3.3 Rounded variants (INFO — likely legitimate table rounding)")
        w("")
        for variant, files in sorted(fx["rounded_variants"].items()):
            w(f"- `{variant}` appears in {len(files)} file(s): "
              + ", ".join(f"`{f}`" for f in files[:6])
              + (" …" if len(files) > 6 else ""))
        w("")
    w("## 4. Verdict")
    w("")
    verdict_ok = fx["all_ok"] and links["dead_count"] == 0
    w(f"- Formula identities: **{'PASS' if fx['all_ok'] else 'FAIL'}** "
      f"({sum(1 for i in fx['identities'] if i[3] == 'OK')}/{len(fx['identities'])})")
    w(f"- Dead links: **{links['dead_count']}** "
      f"({'none — PASS' if links['dead_count'] == 0 else 'see §2 — REPORTED'})")
    w(f"- Inventory: {inv['total']} `.md` files across {len(SECTIONS)} sections + root")
    w("")
    w(f"**Pipeline result: {'CLEAN' if verdict_ok else 'FINDINGS — SEE ABOVE'}**")
    w("")
    w("---")
    w("")
    w("## Appendix A — External links (not fetched)")
    w("")
    w("| Source | URL |")
    w("|---|---|")
    for src, url in links["external"]:
        w(f"| `{src}` | {url} |")
    w("")
    w("## Appendix B — Reproduction")
    w("")
    w("```bash")
    w("/home/error/physics/venv/bin/python tools/run_full_pipeline.py")
    w("```")
    w("")
    w("Key numbers checked (documented in `03_FORMULAS/special_values.md`, "
      "`03_FORMULAS/formula_compendium.md`, `02_FOUNDATIONS/time_dilation.md`):")
    w("")
    w("| Number | Meaning |")
    w("|---|---|")
    w("| `0.80171` | Xi(r_s) = 1 - e^(-phi) — SSZ dilation potential at the Schwarzschild radius |")
    w("| `0.55503` | D(r_s) = 1/(1+Xi(r_s)) — finite SSZ time-dilation factor at r_s (GR: 0) |")
    w("| `1.594811` | r*/r_s decay/global intersection, D_SSZ = D_GR (mass-independent) |")
    w("| `1.386562` | r*/r_s saturation/local intersection (metric-pure form, Delta = 0.0%) |")
    w("")

    report_path = os.path.join(REPO_ROOT, "FULL_PIPELINE_REPORT.md")
    with open(report_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    return report_path


def main() -> int:
    runtime_utc = _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    print(f"SSZ documentation pipeline — {runtime_utc}")
    print(f"Repository: {REPO_ROOT}")
    print()
    print("[1/3] Inventory …")
    inv = step_inventory()
    for sec in SECTIONS:
        n = inv["per_section"][sec]
        print(f"    {sec:<24} {n if n >= 0 else 'MISSING'}")
    print(f"    {'TOTAL .md':<24} {inv['total']} "
          f"(core {inv['core_total']} + paper mirror {inv['papers_mirror_total']})")
    print()
    print("[2/3] Link check …")
    links = step_linkcheck(inv["all"])
    print(f"    links parsed: {links['total_links']}, external: {links['external_count']}, "
          f"anchors: {links['anchor_only']}, DEAD: {links['dead_count']}")
    for src, tgt in links["dead"]:
        print(f"      DEAD  {src} -> {tgt}")
    print()
    print("[3/3] Formula consistency …")
    fx = step_formulacheck(inv["all"])
    for name, got, want, st in fx["identities"]:
        print(f"    [{st}] {name}: computed {got:.6f} vs documented {want}")
    for num in KEY_STRING_NUMBERS:
        print(f"    presence {num}: {len(fx['presence'][num])} files")
    if fx["carrier_gaps"]:
        for carrier, missing in fx["carrier_gaps"]:
            print(f"    GAP {carrier}: missing {missing}")
    else:
        print("    canonical carriers: all four key numbers present")
    print()
    report = write_report(inv, links, fx, runtime_utc)
    size = os.path.getsize(report)
    print(f"Report written: {report} ({size:,} bytes)")
    print()
    print(f"VERDICT: formula identities "
          f"{'PASS' if fx['all_ok'] else 'FAIL'}; dead links {links['dead_count']}; "
          f"inventory {inv['total']} .md files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
