# Consistency Checks

**Status:** CANONICAL

---

## Cross-Repository Consistency

All SSZ repositories must produce consistent results. The following checks are performed:

### 1. Ξ Value Consistency

Every repo that computes Ξ must agree at standard test points:

| r/r_s | Ξ_weak | Ξ_strong | Used in |
|-------|--------|----------|--------|
| 1.0 | 0.500 | **0.802** | metric-pure, unified |
| 1.595 | **0.313** | **0.313** | all repos (intersection) |
| 3.0 | 0.167 | 0.259 | qubits, unified |
| 10.0 | 0.050 | 0.150 | segcalc, lensing |
| 100.0 | 0.005 | — | all repos |

### 2. D Value Consistency

| r/r_s | D_SSZ | D_GR | Δ |
|-------|-------|------|---|
| 1.0 | 0.555 | 0.000 | ∞ |
| 1.595 | 0.611 | 0.611 | 0.0% |
| 3.0 | 0.794 | 0.816 | 2.7% |
| 10.0 | 0.952 | 0.949 | 0.3% |
| 100.0 | 0.995 | 0.995 | 0.0% |

### 3. PPN Consistency

- β = 1 in all repos
- γ = 1 in all repos
- Lensing: α = 2r_s/b (PPN) in all relevant repos
- Shapiro: factor (1+γ) = 2 in all relevant repos

### 4. Regime Boundary Consistency

- Blend zone: 1.8 ≤ r/r_s ≤ 2.2 (not 90-110!)
- C² continuity verified at both boundaries
- No formula mixing without explicit blend

---

## Repo Scope Index

Each repository has a defined scope:

| Repo | Scope | Ξ Formula | PPN? |
|------|-------|-----------|------|
| ssz-qubits | Weak field | r_s/(2r) | NO |
| ssz-metric-pure | Strong field | 1-exp(-φr_s/r) | YES |
| maxwell | Blend | Hermite C² | YES |
| Unified-Results | All regimes | Full | YES |
| segcalc | All regimes | Full | YES |
| freq-curv-validation | Weak field | r_s/(2r) | YES |
| ssz-lensing | Weak-to-strong | Full | YES |

**Rule:** If a repo only covers weak field, don't compare its Ξ values to a strong-field repo — they use different formulas by design.

---

## Common "False Alarm" Patterns

### 1. Factor-2 Discrepancy
**Symptom:** Lensing/Shapiro result is 50% of GR
**Cause:** Using Ξ-only (g_tt) instead of PPN (g_tt + g_rr)
**Fix:** Apply (1+γ) factor

### 2. r*/r_s Mismatch (1.387 vs 1.595)
**Symptom:** Two different intersection points
**Cause:** Different Ξ formulas have different r* values
**Reality:** Both are correct domain markers:
- r*/r_s ≈ 1.595: Ξ_weak ∩ D_GR
- r*/r_s ≈ 1.387: Ξ_strong ∩ D_GR

### 3. Regime Formula Mismatch
**Symptom:** Ξ values differ between repos at same r/r_s
**Cause:** Different repos use different regime formulas
**Fix:** Check which regime each repo covers (see scope table above)

---

## Guardrails ≠ "Repos are wrong"

The repos are **physically correct and internally consistent.** Guardrails prevent:
- Cross-repo confusion from comparing different-scope results
- Silent wrong-method application
- Future misunderstandings when extending the framework

> Guardrails = Documentation hardening, not error correction.

---

© 2025–2026 Carmen N. Wrede, Lino P. Casu
