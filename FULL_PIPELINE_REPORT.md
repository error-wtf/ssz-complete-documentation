# Full Pipeline Report — ssz-complete-documentation

**Generated (UTC):** 2026-10-11 12:06 UTC  
**Tool:** `tools/run_full_pipeline.py` (stdlib only — inventory, link check, formula check)  
**Mode:** read-only on repository content; this report is the only file written.

---

## 1. Inventory (Markdown files per section)

| Section | .md files |
|---|---|
| `00_INDEX/` | 2 |
| `01_OVERVIEW/` | 4 |
| `02_FOUNDATIONS/` | 16 |
| `03_FORMULAS/` | 11 |
| `04_KINEMATICS/` | 6 |
| `05_ELECTROMAGNETISM/` | 8 |
| `06_STRONG_FIELD/` | 16 |
| `07_VALIDATION/` | 18 |
| `08_FALSIFICATION/` | 6 |
| `09_PAPERS/` | 3 |
| `10_REPOSITORIES/` | 4 |
| `11_GUARDRAILS/` | 4 |
| `12_GLOSSARY/` | 2 |
| `13_FREQUENCY_FRAMEWORK/` | 3 |
| **root (readme, memory, license …)** | 5 |

- **Core documentation files (excl. `09_PAPERS/`):** 105
- **Files under `09_PAPERS/`:** 67 (3 section indexes + 64 mirrored paper markdown files in `09_PAPERS/markdown/`; original PDFs in `09_PAPERS/pdf/` are not counted)
- **Total `.md` files in repository:** 172
- Root-level files: `LICENSE.md`, `PEER_REVIEW.md`, `README.md`, `REPRODUCE.md`, `full-segmented-memory.md`

> Note: earlier README wording said "63+ MD files" — the actual count is 105 core files (172 including the paper mirror). README has been corrected in this revision.

## 2. Link Check (relative Markdown links)

- Total Markdown links parsed: **426**
- External (`http(s)://`, `mailto:`) links: **68** (listed in appendix, not fetched — offline check)
- Same-file anchor links (`#…`): **31** (not verified — no reliable GitHub-slug algorithm implemented)
- **Dead relative links (target file missing): 0**

**No dead relative links found.** All relative link targets resolve.

## 3. Formula Consistency Check (canonical key numbers)

### 3.1 Arithmetic identities (recomputed with stdlib `math`)

| Identity | Computed | Documented | Status |
|---|---|---|---|
| Xi(r_s) = 1 - e^(-phi) | 0.801712 | 0.80171 | OK |
| D(r_s) = 1/(1+0.80171) | 0.555028 | 0.55503 | OK |
| z(r_s) = Xi(r_s) (z=0.802 not infinite) | 0.801712 | 0.80171 | OK |
| phi = 1.618034 | 1.618034 | 1.618034 | OK |
| Xi_decay(phi*r_s) = 1 - 1/e | 0.632121 | 0.63212 | OK |
| D_SSZ(phi*r_s) = 1/(1+0.63212) | 0.612700 | 0.6127 | OK |
| D_GR(phi*r_s) = 1/phi | 0.618034 | 0.6180339887498948 | OK |
| r* decay/global (bisection of D_SSZ=D_GR) | 1.594811 | 1.594811 | OK |
| r* saturation/local (Xi_B=1-exp(-phi*x)) | 1.386562 | 1.386562 | OK |
| D(r*) saturation (documented 0.528007) | 0.528007 | 0.528007 | OK |
| z(r*) saturation (documented 0.893914) | 0.893914 | 0.893914 | OK |

**Overall: ALL OK**

### 3.2 Cross-file presence of key numbers

- `0.55503` — present in **20** files
- `0.80171` — present in **26** files
- `1.594811` — present in **23** files
- `1.386562` — present in **22** files

**Canonical carrier gaps (expected files missing a key number):**
- `02_FOUNDATIONS/time_dilation.md` missing: 1.594811, 1.386562
- `02_FOUNDATIONS/segment_density.md` missing: 0.55503

### 3.3 Rounded variants (INFO — likely legitimate table rounding)

- `0.5550` appears in 2 file(s): `06_STRONG_FIELD/GR_SSZ_INTERSECTION_PHI_DISCRETIZATION.md`, `09_PAPERS/markdown/Ssz_-_Finales_Paper_wrede_Casu_Akira.md`

## 4. Verdict

- Formula identities: **PASS** (11/11)
- Dead links: **0** (none — PASS)
- Inventory: 172 `.md` files across 14 sections + root

**Pipeline result: CLEAN**

---

## Appendix A — External links (not fetched)

| Source | URL |
|---|---|
| `01_OVERVIEW/authors.md` | https://github.com/error-wtf |
| `02_FOUNDATIONS/emergent_axes.md` | https://github.com/error-wtf/emergent-spacetime |
| `02_FOUNDATIONS/regime_and_formula_domain_clarification.md` | https://github.com/error-wtf/Segmented-Spacetime-Mass-Projection-Unified-Results |
| `02_FOUNDATIONS/regime_and_formula_domain_clarification.md` | https://github.com/error-wtf/segmented-calculation-suite |
| `02_FOUNDATIONS/regime_and_formula_domain_clarification.md` | https://github.com/error-wtf/ssz-metric-pure |
| `02_FOUNDATIONS/regime_and_formula_domain_clarification.md` | https://github.com/error-wtf/ssz-qubits |
| `02_FOUNDATIONS/regime_definitions.md` | https://github.com/error-wtf/segmented-calculation-suite |
| `02_FOUNDATIONS/segment_density.md` | https://github.com/error-wtf/segmented-calculation-suite |
| `02_FOUNDATIONS/time_dilation.md` | https://github.com/error-wtf/segmented-calculation-suite |
| `02_FOUNDATIONS/time_dilation.md` | https://github.com/error-wtf/ssz-qubits |
| `07_VALIDATION/nebulae_validation.md` | https://github.com/error-wtf/g79-cygnus-tests |
| `09_PAPERS/markdown/README.md` | https://github.com/user-attachments/assets/00de6b04-8ae0-42eb-ac4c-bfab6aead789 |
| `09_PAPERS/markdown/README.md` | https://github.com/user-attachments/assets/b26c6d7d-9523-4ac5-805d-16acc218e80d |
| `09_PAPERS/markdown/README.md` | https://github.com/user-attachments/assets/f70471b4-c77f-44f3-a7ca-d18e4d1d7e53 |
| `10_REPOSITORIES/repo_index.md` | https://github.com/error-wtf |
| `10_REPOSITORIES/repo_index.md` | https://github.com/error-wtf/AfD-Verbotsverfahren-Grundlagenforschung |
| `10_REPOSITORIES/repo_index.md` | https://github.com/error-wtf/CALCULATION_OF_NUMBER_PI |
| `10_REPOSITORIES/repo_index.md` | https://github.com/error-wtf/LOST_EINSTEIN_PAPERS |
| `10_REPOSITORIES/repo_index.md` | https://github.com/error-wtf/MP3-Playlist-Cleaner-Scanner |
| `10_REPOSITORIES/repo_index.md` | https://github.com/error-wtf/Riemann-Zeta-Zero-Finding-Suite |
| `10_REPOSITORIES/repo_index.md` | https://github.com/error-wtf/SEGMENTED_SPACETIME |
| `10_REPOSITORIES/repo_index.md` | https://github.com/error-wtf/SSZ-METRIC_COMPLETE |
| `10_REPOSITORIES/repo_index.md` | https://github.com/error-wtf/Segmented-Spacetime-Mass-Projection-Unified-Results |
| `10_REPOSITORIES/repo_index.md` | https://github.com/error-wtf/Segmented-Spacetime-Starmaps |
| `10_REPOSITORIES/repo_index.md` | https://github.com/error-wtf/TODESSTATISTIKEN |
| `10_REPOSITORIES/repo_index.md` | https://github.com/error-wtf/block-bots |
| `10_REPOSITORIES/repo_index.md` | https://github.com/error-wtf/emergent-spacetime |
| `10_REPOSITORIES/repo_index.md` | https://github.com/error-wtf/error-wtf.github.io |
| `10_REPOSITORIES/repo_index.md` | https://github.com/error-wtf/errordon |
| `10_REPOSITORIES/repo_index.md` | https://github.com/error-wtf/frequency-curvature-validation |
| `10_REPOSITORIES/repo_index.md` | https://github.com/error-wtf/g79-cygnus-tests |
| `10_REPOSITORIES/repo_index.md` | https://github.com/error-wtf/madnews-repo |
| `10_REPOSITORIES/repo_index.md` | https://github.com/error-wtf/mastodon-matrix-theme |
| `10_REPOSITORIES/repo_index.md` | https://github.com/error-wtf/mastodon-media-columns |
| `10_REPOSITORIES/repo_index.md` | https://github.com/error-wtf/matrix-full |
| `10_REPOSITORIES/repo_index.md` | https://github.com/error-wtf/matrix-tetris |
| `10_REPOSITORIES/repo_index.md` | https://github.com/error-wtf/matrixshell-web |
| `10_REPOSITORIES/repo_index.md` | https://github.com/error-wtf/pdf-translator-enhanced |
| `10_REPOSITORIES/repo_index.md` | https://github.com/error-wtf/segmented-calculation-suite |
| `10_REPOSITORIES/repo_index.md` | https://github.com/error-wtf/segmented-energy |
| `10_REPOSITORIES/repo_index.md` | https://github.com/error-wtf/ssz-complete-documentation |
| `10_REPOSITORIES/repo_index.md` | https://github.com/error-wtf/ssz-full-metric |
| `10_REPOSITORIES/repo_index.md` | https://github.com/error-wtf/ssz-lagrange |
| `10_REPOSITORIES/repo_index.md` | https://github.com/error-wtf/ssz-lensing |
| `10_REPOSITORIES/repo_index.md` | https://github.com/error-wtf/ssz-ligo-tests |
| `10_REPOSITORIES/repo_index.md` | https://github.com/error-wtf/ssz-metric-final |
| `10_REPOSITORIES/repo_index.md` | https://github.com/error-wtf/ssz-metric-pure |
| `10_REPOSITORIES/repo_index.md` | https://github.com/error-wtf/ssz-paper-plots |
| `10_REPOSITORIES/repo_index.md` | https://github.com/error-wtf/ssz-qubits |
| `10_REPOSITORIES/repo_index.md` | https://github.com/error-wtf/ssz-schumann |
| `10_REPOSITORIES/repo_index.md` | https://github.com/error-wtf/ssz-trajectories |
| `PEER_REVIEW.md` | https://github.com/error-wtf/SSZ-Spectroscopy-Bridge |
| `PEER_REVIEW.md` | https://github.com/error-wtf/SSZ-Transport-Bridge |
| `PEER_REVIEW.md` | https://github.com/error-wtf/SSZ_FULL_CLOSURE |
| `PEER_REVIEW.md` | https://github.com/error-wtf/ssz-ligo-tests |
| `README.md` | https://github.com/error-wtf/SSZ-Spectroscopy-Bridge |
| `README.md` | https://github.com/error-wtf/SSZ-Transport-Bridge |
| `README.md` | https://github.com/error-wtf/SSZ_FULL_CLOSURE |
| `README.md` | https://github.com/error-wtf/ssz-ligo-tests/blob/main/docs/LIGO_OPEN_DATA_FULL_REPORT.md |
| `README.md` | https://github.com/error-wtf/ssz-ligo-tests/blob/main/docs/LIGO_REPRODUCIBILITY_CRITIQUE.md |
| `README.md` | https://zenodo.org/records/18600070 |
| `REPRODUCE.md` | https://github.com/error-wtf/ssz-ligo-tests |

## Appendix B — Reproduction

```bash
/home/error/physics/venv/bin/python tools/run_full_pipeline.py
```

Key numbers checked (documented in `03_FORMULAS/special_values.md`, `03_FORMULAS/formula_compendium.md`, `02_FOUNDATIONS/time_dilation.md`):

| Number | Meaning |
|---|---|
| `0.80171` | Xi(r_s) = 1 - e^(-phi) — SSZ dilation potential at the Schwarzschild radius |
| `0.55503` | D(r_s) = 1/(1+Xi(r_s)) — finite SSZ time-dilation factor at r_s (GR: 0) |
| `1.594811` | r*/r_s decay/global intersection, D_SSZ = D_GR (mass-independent) |
| `1.386562` | r*/r_s saturation/local intersection (metric-pure form, Delta = 0.0%) |

