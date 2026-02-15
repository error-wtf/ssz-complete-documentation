# Cross-Repository Consistency Checks

---

## Repository Test Summary

| # | Repository | Tests | Pass Rate |
|---|-----------|-------|-----------|
| 1 | ssz-metric-pure | 10/10 | 100% |
| 2 | ssz-lensing | 28/28 | 100% |
| 3 | ssz-qubits | 74 | 100% |
| 4 | frequency-curvature-validation | 11/11 | 100% |
| 5 | g79-cygnus-tests | 14/14 | 100% |
| 6 | Unified-Results | 25/25 suites | 100% |
| 7 | ssz-schumann | 94 | 100% |
| 8 | segmented-calculation-suite | 24 | 100% |
| 9 | ssz-paper-plots | 6 | 100% |
| 10 | segmented-energy | 3 | 100% |
| 11 | Starmaps | 46 | 100% |
| **TOTAL** | | **747+** | **100%** |

---

## Cross-Repository Consistency

Same formulas across all repos produce identical results:
- Ξ_weak = r_s/(2r) → consistent everywhere
- D = 1/(1+Ξ) → consistent everywhere
- PPN γ = β = 1 → consistent everywhere

---

## Repo Scope Index

| Repo | Scope | Ξ Formula | PPN? |
|------|-------|-----------|------|
| ssz-qubits | Weak | r_s/(2r) | NO |
| ssz-metric-pure | Strong | 1-exp(-φr_s/r) | YES |
| maxwell | Blend | Hermite C² | YES |
| Unified-Results | Strong | Ξ_max(1-exp(...)) | YES |
| frequency-curvature | Weak+PPN | r_s/(2r) | YES |
| ssz-lensing | Weak+PPN | Radial scaling | YES |

**Critical:** Different repos have different scopes. Don't compare results across repos without checking which regime and method each uses.
