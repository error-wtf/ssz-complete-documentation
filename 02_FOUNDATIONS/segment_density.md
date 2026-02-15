# Segment Density Ξ(r)

The central quantity of SSZ. Quantifies how "segmented" spacetime is at radial coordinate r from a mass M.

---

## Weak Field (r/r_s > 10)

```
Ξ_weak(r) = r_s / (2r)
```

- **Origin:** PPN expansion with β = γ = 1
- **Unit check:** [m]/[m] = dimensionless ✓
- **Papers:** 01 (Radial Scaling), 03 (Frequency Framework)
- **Tests:** `test_ppn_exact.py`, `test_weak_field_contract.py`

| Object | r/r_s | Ξ_weak |
|--------|-------|---------|
| Earth surface | ~7×10⁸ | ~7×10⁻¹⁰ |
| Sun surface | ~5×10⁵ | ~10⁻⁶ |
| White dwarf | ~10³ | ~5×10⁻⁴ |
| GPS satellite | ~10⁹ | ~5×10⁻¹⁰ |

---

## Strong Field (r/r_s < 1.8)

```
Ξ_strong(r) = 1 - exp(-φ × r_s / r)
```

where φ = (1+√5)/2 = 1.618033988749895

- **Origin:** Horizon regularity, φ-geometry
- **Limits:** Ξ(r→∞) → 0, Ξ(r_s) = 1 - exp(-φ) = 0.80171
- **Papers:** 04 (Metric), 16 (Singularity)
- **Tests:** `test_horizon_finite.py`, `test_xi_strong.py`

| r/r_s | Ξ_strong |
|-------|----------|
| 1.0 | 0.80171 |
| 1.5 | 0.66010 |
| 2.0 | 0.55347 |
| 3.0 | 0.41476 |
| 5.0 | 0.27631 |

---

## Blend Zone (1.8 ≤ r/r_s ≤ 2.2)

```
t = (r/r_s - 1.8) / 0.4     (normalized to [0,1])
Ξ_blend(r) = H₅(t)           (Quintic Hermite)
```

C⁰ + C¹ + C² continuous. **Test:** `test_c2_segments_strict.py`

---

## Regime Summary

| Regime | r/r_s | Formula |
|--------|-------|---------|
| very_close | < 1.8 | Ξ_strong |
| blended | 1.8–2.2 | Hermite C² |
| photon_sphere | 2.2–3.0 | Ξ_strong |
| strong | 3.0–10.0 | Ξ_strong |
| weak | > 10.0 | Ξ_weak |

**WARNING:** Values 90/110 in some code are PROBE_RADII, NOT regime boundaries!

---

## DEPRECATED (FORBIDDEN)

```
❌ Ξ = (r_s/r)² × exp(-r/r_φ)    ← BANNED
```
