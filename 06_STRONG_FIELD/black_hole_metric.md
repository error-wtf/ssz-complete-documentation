# Complete Black Hole Metric

**Paper:** 04 (Segmented Spacetime: On the Metric of Black Holes)

---

## SSZ Metric

The SSZ metric modifies the Schwarzschild metric through the segment density:

```
ds² = -D²(r) c² dt² + s²(r) dr² + r² dΩ²

where:
  D(r) = 1/(1 + Ξ(r))    time dilation
  s(r) = 1 + Ξ(r)         scaling factor
  dΩ² = dθ² + sin²θ dφ²
```

---

## Key Difference from GR

| Property | Schwarzschild (GR) | SSZ |
|----------|-------------------|-----|
| g_tt at r_s | 0 (singular) | D² = 0.308 (finite) |
| g_rr at r_s | ∞ (singular) | s² = 3.24 (finite) |
| Curvature at r_s | Finite (Kretschner) | Finite |
| Light cones at r_s | Close | Modified but regular |

---

## 4D Tensor Formulation (ssz-metric-pure)

- **Metric tensor:** g_μν (4×4) + inverse g^μν
- **Christoffel symbols:** Γ^ρ_μν (10 non-zero components)
- **Einstein tensor:** G^μ_ν (4 components, mixed indices)
- **Ricci tensor:** R_μν + scalar R
- **Kretschmann scalar:** K (finite everywhere, singularity-free)

---

## 2PN Calibration (v2.1.0)

```
φ²_G(r) = 2U(1 + U/3),  U = GM/(rc²)
```

- 100× faster convergence than 1PN
- GPS redshift: < 0.05% error
- Pound-Rebka: exact match

---

## Validation: 10/10 PASS

| Test | Target | Status |
|------|--------|--------|
| Asymptotic flatness | ≤10⁻⁶ | ✅ |
| GPS redshift | ≤0.1% | ✅ |
| Pound-Rebka | ≤0.1% | ✅ |
| Shapiro delay | ≤5% | ✅ |
| Light deflection | ≤10% | ✅ |
| Metric compatibility | ≤10⁻¹³ | ✅ |
| Energy conservation | ≤10⁻¹² | ✅ |
| Light cone closing | Monotonic | ✅ |
| Curvature invariants | Finite | ✅ |
| SSZ kernel elements | γ,β,φ | ✅ |
