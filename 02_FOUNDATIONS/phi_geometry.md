# φ-Geometry in SSZ

---

## Not Numerology — A Constraint

φ serves as a structural constraint that:
1. Reduces parameter arbitrariness
2. Maintains consistent fits across strong-field observables
3. Generates regime transition from a single scaling principle

---

## φ in SSZ Formulas

### Strong-Field Ξ
```
Ξ_strong(r) = 1 - exp(-φ · r_s / r)
```

### Saturation Value
```
Ξ(r_s) = 1 - e^(-φ) = 0.80171
```

### Coupling Radius
```
r_φ = (φ/2) · r_s · [1 + β · Δ(M)]
```

### Redshift Lattice
```
R = 1 + z = φ^N,   N ∈ ℤ
```

### Euler Embedding (Paper 06)
```
z_k = r₀ · e^{k(ln φ + iΔθ)}
r(θ) = r₀ · e^{bθ},  b = ln φ / Δθ ≈ 0.306
```

---

## Mass-Dependent Correction Δ(M)

```
Δ(M) = A · exp(-α / M^B)

A = 98.01,  α = 2.7177 × 10⁴,  B = 1.96
```

Derived from φ-geometry, **NOT** data fitting. Paper 18, Test: `test_phi_correction.py`
