# Segmented Spacetime (SSZ) — Complete Documentation

**Authors:** Carmen N. Wrede, Lino P. Casu
**AI Assistants:** Bingsi, Akira
**Status:** Canonical Reference — Single Source of Truth
**Last Updated:** 2026-02-15

---

## What is SSZ?

Segmented Spacetime (SSZ) is a falsifiable extension of General Relativity (GR) built around a single additional quantity: a **dimensionless segment density field Ξ(r)**. SSZ reproduces GR exactly in weak fields while producing systematic, testable deviations in strong fields — especially around neutron stars and compact objects.

**Core equation:**
```
D_SSZ(r) = 1 / (1 + Ξ(r))
```

At the Schwarzschild radius: **D(r_s) = 0.555** (finite!) vs GR: D(r_s) = 0 (singularity).

---

## Documentation Structure

| # | Section | Contents |
|---|---------|----------|
| 01 | [Overview](01_OVERVIEW/) | What is SSZ, core postulates, relation to GR |
| 02 | [Foundations](02_FOUNDATIONS/) | Ξ(r), D(r), regimes, φ-geometry |
| 03 | [Formulas](03_FORMULAS/) | Complete formula compendium, symbol table, quick reference |
| 04 | [Kinematics](04_KINEMATICS/) | Dual velocities, Lorentz v=0, kinematic closure |
| 05 | [Electromagnetism](05_ELECTROMAGNETISM/) | Maxwell gauge, rotating space, group velocity, redshift |
| 06 | [Strong Field](06_STRONG_FIELD/) | BH metric, singularities, cosmic censorship, dark star |
| 07 | [Validation](07_VALIDATION/) | Test methodology, cross-repo results, GR vs SSZ tables |
| 08 | [Falsification](08_FALSIFICATION/) | Testable predictions, instruments, falsification criteria |
| 09 | [Papers](09_PAPERS/) | All 25 papers, bibliography, preprints |
| 10 | [Repositories](10_REPOSITORIES/) | All 35 repos, test index, reproducibility |
| 11 | [Guardrails](11_GUARDRAILS/) | Prime directive, method assignment, confusion prevention |
| 12 | [Glossary](12_GLOSSARY/) | EN/DE terminology |

---

## Key Numbers

| Metric | Value |
|--------|-------|
| Papers | 25 primary + 7 additional |
| Repositories | 35 total (17 SSZ, 2 math, 3 research, 3 tools, 8 web, 2 private) |
| Tests | 747+ validated, 200+ test files |
| Documentation files | 1,803+ across all repos |
| Consistency checks | 171/171 PASS |
| Book chapters | 30 (8 parts + appendices A–G) |
| Manuscript | ~90,000 words, ~300 pages |

---

## Quick Start

1. **New to SSZ?** → Start with [01_OVERVIEW/ssz_overview.md](01_OVERVIEW/ssz_overview.md)
2. **Need formulas?** → Go to [03_FORMULAS/formula_compendium.md](03_FORMULAS/formula_compendium.md)
3. **Quick card** → See [03_FORMULAS/quick_reference.md](03_FORMULAS/quick_reference.md)
4. **Method selection** → Read [11_GUARDRAILS/prime_directive.md](11_GUARDRAILS/prime_directive.md)
5. **Validation data** → Check [07_VALIDATION/gr_vs_ssz_tables.md](07_VALIDATION/gr_vs_ssz_tables.md)
6. **Reproduce results** → Follow [10_REPOSITORIES/reproducibility.md](10_REPOSITORIES/reproducibility.md)

---

## The SSZ Mantra

> **Observable → Class → Method → Scope → Then calculate.**

| Observable Type | Method | Formula |
|----------------|--------|---------|
| Timelike (clocks) | Ξ-based | D = 1/(1+Ξ) |
| Null (light) | PPN (1+γ) | α = 2r_s/b |
| Orbit (precession) | PPN (β,γ) | Standard PPN |

---

## License

Anti-Capitalist Software License v1.4

© 2025–2026 Carmen N. Wrede, Lino P. Casu
