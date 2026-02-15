# Time Dilation D(r)

---

## Definition

```
D_SSZ(r) = 1 / (1 + Ξ(r))
dτ = D_SSZ(r) · dt
```

---

## Comparison with GR

```
D_GR(r) = √(1 - r_s/r)
D_GR(r_s) = 0    → SINGULARITY
D_SSZ(r_s) = 0.555 → FINITE
```

---

## Values Across Object Classes

| Object | r/r_s | D_GR | D_SSZ | Δ(%) | Regime |
|--------|-------|------|-------|------|--------|
| Earth | ~7×10⁸ | 0.9999999993 | 0.9999999993 | ~0% | weak |
| Sun | ~5×10⁵ | 0.999999 | 0.999999 | ~0% | weak |
| GPS satellite | ~10⁹ | 0.99999999994 | 0.99999999994 | ~0% | weak |
| S2 star | ~2800 | 0.99982 | 0.99982 | <0.01% | weak |
| PSR J0030+0451 | 3.06 | 0.819 | 0.790 | **-3.5%** | strong |
| PSR J0740+6620 | 2.23 | 0.742 | 0.697 | **-6.1%** | strong |
| PSR J0348+0432 | 2.10 | 0.724 | 0.674 | **-6.9%** | strong |
| Intersection | 1.595 | 0.611 | 0.611 | **0.0%** | blend |
| Schwarzschild | 1.00 | 0.000 | **0.555** | **∞** | very_close |

---

## Scaling Factor

```
s(r) = 1 + Ξ(r) = 1 / D(r)
```

Maxwell field scaling: E'(r) = s(r) · E(r), B'(r) = s(r) · B(r)

---

## Gravitational Redshift

```
z_SSZ(r) = 1/D(r) - 1 = Ξ(r)
```

**Identity:** z ≡ Ξ (direct equivalence)
