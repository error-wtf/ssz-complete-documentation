# PEER_REVIEW — Documentation Review Notes

Review scope: `ssz-complete-documentation` (172 MD files as of 2026-10-11, see [FULL_PIPELINE_REPORT.md](FULL_PIPELINE_REPORT.md)). This file documents where the core formulas live, which numbers are load-bearing, where the documentation has known tensions, and how this repo relates to the numerical research repositories.

---

## 1. Where the core formulas are documented

| Concept | Canonical source | Status |
|---|---|---|
| Segment density Ξ(r), weak/strong branches | `02_FOUNDATIONS/segment_density.md` | CANONICAL |
| Time dilation `D = 1/(1+Ξ)`, `dτ = D·dt` | `02_FOUNDATIONS/time_dilation.md` | CANONICAL |
| Regime definitions (5 regimes, blend 1.8–2.2 r/r_s, Hermite C²) | `02_FOUNDATIONS/regime_definitions.md` | CANONICAL |
| φ-geometry, φ-lattice x_k = φ^k, bracket theorem | `02_FOUNDATIONS/phi_geometry.md`, `02_FOUNDATIONS/phi_lattice_discretization.md` | CANONICAL |
| r*/r_s intersections: 1.594811 (decay), 1.386562 (saturation) | `02_FOUNDATIONS/intersection_invariance.md` | CANONICAL |
| Special values table (Ξ(r_s)=0.80171, D(r_s)=0.55503, φ-table) | `03_FORMULAS/special_values.md` | CANONICAL |
| Full formula compendium with origin + domain | `03_FORMULAS/formula_compendium.md` | CANONICAL |
| PPN formulas (γ=1 for light!) | `03_FORMULAS/ppn_formulas.md` | **CRITICAL** |
| Regime vs formula-domain distinctions (6 misunderstandings) | `02_FOUNDATIONS/regime_and_formula_domain_clarification.md` | CANONICAL |
| Deprecated formulas to avoid | `03_FORMULAS/forbidden_formulas.md` | reference |

## 2. Load-bearing numbers (critical)

| Number | Meaning | Verified by |
|---|---|---|
| **0.55503** | D(r_s): SSZ time dilation at the Schwarzschild radius (GR: 0) | Pipeline identity check; documented in 18–21 canonical files |
| **0.80171** | Ξ(r_s) = 1/D(r_s) − 1 | Pipeline identity check |
| **1.594811** | r*/r_s, decay branch: `1/(1+Ξ_strong) = sqrt(1−1/x)` on [1, φ] | Bisection, pipeline check |
| **1.386562** | r*/r_s, saturation branch: `1/(2−exp(−φ·x)) = sqrt(1−1/x)`, D=0.528007, z=0.893914 | Bisection, pipeline check |
| **γ = 1** (PPN) | Null observables stay GR — the falsifiability firewall | `03_FORMULAS/ppn_formulas.md` |
| **1296/1296** | All-tests canonical pass count (2026-05-07 snapshot) | `07_VALIDATION/all_tests_2026-05-07.md` |

The pipeline's formula check recomputes 11 identities from first principles and compares to the documented values (tolerances down to 1e-12 for construction constants, 1e-5 for bisection roots). Latest run: 11/11 OK.

## 3. Known tensions / caveats in the documentation

1. **Regime mixing is the #1 error source.** Weak/strong Ξ branches have disjoint domains; the 1.8–2.2 r/r_s band is a C² Hermite blend, not a formula mix. `02_FOUNDATIONS/regime_and_formula_domain_clarification.md` lists 6 documented misunderstandings — consult it before any calculation.
2. **Timelike vs null observables.** Clocks use Ξ-based D; light uses PPN (1+γ) with γ=1. Mixing these invalidates results (see `11_GUARDRAILS/prime_directive.md`). Example tension: `07_VALIDATION/ligo_gw240925_v0_pipeline.md` is explicitly **EXPLORATORY, no claim** — it must not be cited as validation.
3. **LIGO critique documents are external.** `08_FALSIFICATION` references two documents that exist only in the [ssz-ligo-tests](https://github.com/error-wtf/ssz-ligo-tests) repo (reproducibility critique; open-data full report). The 2026-10-11 link audit found the relative links dead and re-pointed them to GitHub URLs (documented in the README; pipeline reports both as historical dead links).
4. **Paper-mirror duplication.** `09_PAPERS/markdown/` mirrors 64 papers as markdown next to `pdf/` sources. This is intentional (searchability) but means counts like "170 files" include mirrors; the pipeline separates core (103) from mirror (67) counts to avoid inflated impressions.
5. **Snapshot dating.** `07_VALIDATION/all_tests_2026-05-07.md` is a point-in-time snapshot; the 2026-10-11 re-certification facts (below) live in the research repos, not in this documentation repo.

## 4. Relation to research repositories

Numerical work is deliberately separated from documentation:

| Repository | Role | 2026-10-11 re-certification (documented in SSZ_FULL_CLOSURE) |
|---|---|---|
| [SSZ_FULL_CLOSURE](https://github.com/error-wtf/SSZ_FULL_CLOSURE) | Full-closure numerical program (FK coupled model, SRF, bridge runs) — carries the re-certification record | FK V1 **6/6 gates PASS**; SRF **5/5 gates PASS**; Bridge Run 6 **STAGE1+STAGE2 PASS**; SW-Diag **PEAKS_NOT_ROBUST** |
| [SSZ-Transport-Bridge](https://github.com/error-wtf/SSZ-Transport-Bridge) | Transport-bridge calculations | — (certified via SSZ_FULL_CLOSURE record) |
| [SSZ-Spectroscopy-Bridge](https://github.com/error-wtf/SSZ-Spectroscopy-Bridge) | Spectroscopy-bridge (QNM/ε-220 program) | — (certified via SSZ_FULL_CLOSURE recall of the closure record) |
| [ssz-ligo-tests](https://github.com/error-wtf/ssz-ligo-tests) | LIGO open-data tests; hosts the critique documents referenced by `08_FALSIFICATION` | — |

**Review note:** the SW-Diag verdict **PEAKS_NOT_ROBUST** is a negative/limiting result — it bounds which claims may be made from that diagnostic. Cite it as such, not as a pass.

## 5. Review checklist for future edits

- [ ] Any new number added to `03_FORMULAS/special_values.md` is cross-checked against `02_FOUNDATIONS/` derivations.
- [ ] Regime/domain check performed before using any Ξ formula (see the mandatory rule above).
- [ ] Relative links resolve (run the pipeline; investigate anything new in the dead-link list).
- [ ] Counts in README updated when files are added/removed (pipeline inventory).
- [ ] Exploratory material stays labeled EXPLORATORY / no-claim.
- [ ] Research-repo facts are cited to the repo that documents them (SSZ_FULL_CLOSURE for re-certification).
