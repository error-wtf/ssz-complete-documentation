# Test Methodology & Anti-Circularity

**Papers:** Chapter 26 of the SSZ Book

---

## Anti-Circularity Proof

The dependency graph of SSZ is **acyclic** (Level 0 → Level 5):

| Level | Contents |
|-------|----------|
| 0 | External constants (c, G, ℏ, φ, π) from CODATA/BIPM/math |
| 1 | r_s = 2GM/c² (from Level 0) |
| 2 | Ξ formulas (from Level 0 + 1) |
| 3 | D, z, s (from Level 2) |
| 4 | PPN observables (from Level 2 + 3) |
| 5 | Predictions and comparisons (from Level 3 + 4) |

**No circular dependencies.** Validation data was never used for calibration.

---

## Test Infrastructure

| Metric | Value |
|--------|-------|
| Test files | 200+ |
| Functions | 1,128 |
| Assertions | ~1,918 |
| Repositories | 13 |
| Pass rate | 100% (171/171 documented) |

---

## Test Categories

1. **PPN tests:** γ=β=1, Shapiro, lensing, perihelion
2. **Dual velocity tests:** v_esc × v_fall = c²
3. **C¹/C² continuity:** Blend zone smoothness
4. **Energy conditions:** WEC, DEC, SEC
5. **Real-data validation:** GPS, Pound-Rebka, S2, NICER neutron stars
6. **Cross-platform:** Results consistent across all repos

---

## What Tests Prove (and Don't)

**Tests prove:**
- Internal mathematical consistency
- GR recovery in weak field
- Smooth regime transitions
- Correct PPN parameters
- Agreement with experimental data where SSZ = GR

**Tests do NOT prove:**
- That SSZ is the correct theory of gravity
- That strong-field predictions are correct (untested)
- That φ is fundamentally necessary

The tests establish that SSZ is **self-consistent and GR-compatible**, not that it is "true."

**Source:** `segmented-calculation-suite/docs/ANTI_CIRCULARITY.md`
