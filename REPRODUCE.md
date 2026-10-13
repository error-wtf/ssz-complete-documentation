# REPRODUCE — Animations & Pipeline

How to re-derive everything this repository's tooling produces: the core-physics animation GIFs and the full documentation-pipeline report. All commands were verified on 2026-10-11 with the environment below.

---

## Environment

| Item | Value |
|---|---|
| Python | venv at `/home/error/physics/venv/bin/python` |
| numpy | 2.5.3 |
| matplotlib | 3.11.2 |
| pillow | 12.3.0 |
| OS | Linux (Kali) |

The animation renderer needs numpy + matplotlib + pillow. The pipeline runner is **stdlib-only** (no third-party imports).

---

## 1. Core Physics Animations

```bash
cd /path/to/ssz-complete-documentation
/home/error/physics/venv/bin/python demos/render_core_physics_animations.py
```

- Writes 3 GIFs to `demos/output/` (dark theme, English labels).
- Runs built-in self-checks after rendering (formula endpoint values, C0/C2 blend continuity, lattice/bracket identities). **Exit code 0 = all checks passed.**
- Typical runtime: ~1–2 min.

### Outputs

| File | Frames | fps | Content |
|---|---|---|---|
| `demos/output/ssz_time_dilation_gr_vs_ssz.gif` | 76 | 10 | Time-dilation factor D(r): GR `sqrt(1−r_s/r)` → 0 at r_s vs SSZ `D = 1/(1+Ξ(r))` → **0.55503** at r_s; curves built up dynamically |
| `demos/output/ssz_regime_map_animated.gif` | 80 | 9 | Weak/strong regime map in r/r_s with transition radii fading in: very close (<1.8), Hermite-C² blend (1.8–2.2), photon sphere (2.2–3.0), strong (3.0–10.0), weak (>10.0) |
| `demos/output/ssz_phi_lattice_bracket_theorem.gif` | 66 | 8 | φ-lattice sites x_k = φ^k growing + bracket-theorem intervals [F_k, F_k+1] around each site |

### Formulas used (and where they are documented)

Every formula in the renderer is taken verbatim from the canonical documentation — the module docstring of `demos/render_core_physics_animations.py` cites the exact source files:

| Formula | Canonical source |
|---|---|
| `D_SSZ(r) = 1/(1+Ξ(r))`, `dτ = D·dt` | `02_FOUNDATIONS/time_dilation.md`, `02_FOUNDATIONS/segment_density.md` |
| `Ξ_weak = r_s/(2r)`, `Ξ_strong = 1−exp(−φ·r_s/r)` | `02_FOUNDATIONS/segment_density.md` |
| Regime boundaries + quintic Hermite blend H5 (C²) | `02_FOUNDATIONS/regime_definitions.md` |
| Ξ(r_s) = 0.80171, D(r_s) = 0.55503 | `03_FORMULAS/special_values.md` |
| r*/r_s = 1.594811 (decay branch) and 1.386562 (saturation branch) | `02_FOUNDATIONS/intersection_invariance.md` |
| x_k = φ^k, bracket theorem [F_k, F_k+1] | `02_FOUNDATIONS/phi_lattice_discretization.md` |
| Full compendium / cross-checks | `03_FORMULAS/formula_compendium.md` |

**Regime rule (mandatory):** never evaluate Ξ without the regime check — weak/strong branches are only valid in their domains; the 1.8–2.2 r/r_s band is bridged by the documented C² Hermite blend, not by mixing formulas.

### Verifying the GIFs programmatically

The renderer's self-checks assert the physics values (e.g. D(r_s) = 0.55503 within 1e-12 of construction). For pixel-level verification, extract the last frame of each GIF with pillow and check the dark background and curve colors (SSZ blue `#58a6ff`, GR red `#f85149`, green `#3fb950`, amber `#d29922`, purple `#a371f7`; background `(13,17,23)`/`(22,27,34)`).

---

## 2. Full Pipeline & Report

```bash
cd /path/to/ssz-complete-documentation
/home/error/physics/venv/bin/python tools/run_full_pipeline.py
```

Writes `FULL_PIPELINE_REPORT.md` at the repo root (the report excludes itself from the inventory so counts are stable across runs).

### What it checks

1. **Inventory** — counts MD files per section directory; separates core documentation from the `09_PAPERS/` mirror (`markdown/` holds 64 mirrored papers; PDFs are not counted).
2. **Link check** — resolves every relative Markdown link in every MD file; dead targets are **listed, never silently fixed** (policy: only typos in newly created files may be corrected).
3. **Formula consistency** — recomputes the canonical key numbers from first principles (bisection where needed) and compares against the documented values, then counts cross-file presence of each number (including rounded variants, deduplicated per file):
   - Ξ(r_s) = 0.80171
   - D(r_s) = 0.55503
   - r*/r_s = 1.594811 — decay branch: root of `1/(1+Ξ_strong(x)) = sqrt(1−1/x)` on the bracket-theorem interval [1, φ]
   - r*/r_s = 1.386562 — saturation branch: root of `1/(2−exp(−φ·x)) = sqrt(1−1/x)`, with D(r*) = 0.528007 and z(r*) = 0.893914 (`02_FOUNDATIONS/intersection_invariance.md`)

### Expected results (2026-10-11 run, after this revision)

- Formula identities: **11/11 OK**
- Dead relative links: **0** (the two historical dead links in the pre-revision README pointed at `08_FALSIFICATION/ligo_reproducibility_critique.md` and `08_FALSIFICATION/ligo_open_data_full_report.md` — targets that exist only in the external [ssz-ligo-tests](https://github.com/error-wtf/ssz-ligo-tests) repo; the 2026-10-11 README revision re-pointed them openly to their GitHub URLs)
- Inventory: 172 MD files after this revision (105 core + 67 papers-section = 3 indexes + 64 mirrors; the revision added `REPRODUCE.md` and `PEER_REVIEW.md`)

### Audit trail of the 2026-10-11 revision

| Finding | Resolution |
|---|---|
| README claimed "63+ MD files" | Corrected: real count 172 (105 + 67), verified by pipeline |
| 12+ files on disk missing from the README index | Added to the index |
| 2 dead LIGO links (targets only in external repo) | Listed in report; README re-pointed to GitHub URLs with inline notes |
| `ligo_h1l1_long_baseline_plan.md` listed in README but never existed as a file | Merged into the test-plan entry with an explanatory note |

---

## 3. Numerical spot-checks (optional)

The saturation-branch identity can be re-derived in one line:

```python
/home/error/physics/venv/bin/python - <<'EOF'
from math import exp, sqrt, phi
f = lambda x: 1/(2 - exp(-phi*x)) - sqrt(1 - 1/x)
lo, hi = 1.0, 1.6                      # sign change bracket
for _ in range(200):
    mid = (lo + hi)/2
    if f(lo)*f(mid) <= 0: hi = mid
    else: lo = mid
x = (lo + hi)/2
print(f"x={x:.6f}  D={1/(2-exp(-phi*x)):.6f}  z={1/(1/(2-exp(-phi*x)))-1:.6f}")
# -> x=1.386562  D=0.528007  z=0.893914
EOF
```

---

## 4. What is intentionally NOT done here

- No git commits (documentation-only working state).
- No edits to canonical physics content (`02_FOUNDATIONS/`, `03_FORMULAS/`) — the pipeline reads, never writes, those files.
- Dead links in pre-existing files are reported only; the single exception (the two LIGO links re-pointed in README) is documented inline in the README and in the table above.
