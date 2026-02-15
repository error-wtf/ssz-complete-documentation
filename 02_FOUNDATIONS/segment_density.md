# Segment Density Ξ(r)

**Status:** CANONICAL

---

## Definition

The segment density Ξ (Xi) is the central quantity in SSZ. It is a dimensionless, non-negative scalar field that measures the degree of spacetime segmentation at radial coordinate r from a gravitating mass M.

```
Ξ(r) ≥ 0    for all r
Ξ(r) → 0    as r → ∞
Ξ(r) ≤ Ξ_max = 1 - e^(-φ) ≈ 0.802
```

---

## Weak-Field Formula (g1)

**Validity:** r/r_s > 10 (in practice, essentially all Solar System scales)

```
Ξ_weak(r) = r_s / (2r)
```

where r_s = 2GM/c² is the Schwarzschild radius.

**Properties:**
- Recovers GR time dilation to arbitrary precision
- Monotonically decreasing with r
- At Earth surface: Ξ ≈ 7 × 10⁻¹⁰
- At Sun surface: Ξ ≈ 2 × 10⁻⁶
- At GPS orbit: Ξ ≈ 7 × 10⁻¹⁰

---

## Strong-Field Formula (g2)

**Validity:** r/r_s < 1.8

```
Ξ_strong(r) = 1 - exp(-φ · r_s / r)
```

where φ = (1+√5)/2 = 1.618033988749895 is the golden ratio.

**Properties:**
- Saturates at Ξ_max as r → 0 (no divergence!)
- Monotonically decreasing with r
- At Schwarzschild radius: Ξ(r_s) = 1 - e^(-φ) = 0.80171
- Continuous and smooth

---

## Blend Zone (Hermite C² Interpolation)

**Validity:** 1.8 ≤ r/r_s ≤ 2.2

```
t = (r/r_s - 1.8) / 0.4
Ξ_blend(r) = H₅(t)
```

The Hermite quintic interpolation H₅(t) ensures:
- Ξ is continuous at both boundaries
- dΞ/dr is continuous (C¹)
- d²Ξ/dr² is continuous (C²)

```
H₅(t) = (1-t)³(1+3t+6t²)·Ξ_strong(1.8·r_s) + t³(1+3(1-t)+6(1-t)²)·Ξ_weak(2.2·r_s)
         + derivative matching terms
```

This is not a free choice — it is the unique C² interpolant matching both function values and first two derivatives.

---

## Regime Boundaries Summary

| Regime | r/r_s | Ξ formula | Description |
|--------|-------|-----------|-------------|
| very_close | < 1.8 | Ξ_strong | Near/at horizon |
| blended | 1.8–2.2 | H₅(t) | Smooth transition |
| photon_sphere | 2.2–3.0 | Ξ_strong | SSZ optimal zone |
| strong | 3.0–10.0 | Ξ_strong | Measurable deviations |
| weak | > 10.0 | Ξ_weak | GR-identical |

---

## Key Values

| Location | r/r_s | Ξ_weak | Ξ_strong | Used |
|----------|-------|--------|----------|------|
| Earth surface | ~7×10⁸ | 7×10⁻¹⁰ | — | weak |
| Sun surface | ~5×10⁵ | 1×10⁻⁶ | — | weak |
| S2 perihelion | ~2800 | 1.8×10⁻⁴ | — | weak |
| Neutron star | ~2–3 | 0.167–0.250 | 0.259–0.506 | strong |
| Intersection r* | 1.595 | 0.313 | 0.313 | both equal |
| Schwarzschild | 1.0 | 0.500 | **0.802** | strong |

---

## The Intersection Point r*

The two Ξ formulas cross at exactly:
```
r*/r_s = 1.59481
Ξ_weak(r*) = Ξ_strong(r*) = 0.31350
D(r*) = 0.61071
```

This intersection is:
- **Mass-independent** (purely geometric)
- **Derived**, not fitted
- The natural regime-transition marker

---

## DEPRECATED Formula (FORBIDDEN)

```
❌ Ξ = (r_s/r)² × exp(-r/r_φ)   — VERBOTEN
```

This old formula appears in some early drafts. It is **permanently deprecated** and must never be used in any new calculation or derivation.

---

## Cross-References

- Time dilation: `02_FOUNDATIONS/time_dilation.md`
- Regime definitions: `02_FOUNDATIONS/regime_definitions.md`
- Full formula list: `03_FORMULAS/formula_compendium.md`
- Test: `test_xi_calculations.py`, `test_xi_strong.py` in segmented-calculation-suite

---

© 2025–2026 Carmen N. Wrede, Lino P. Casu
