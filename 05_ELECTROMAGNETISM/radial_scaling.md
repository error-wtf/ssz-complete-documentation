# Radial Scaling Gauge for Maxwell Fields

**Paper:** 01 (Radial Scaling Gauge for Maxwell Fields)

---

## The Scaling Factor

```
s(r) = 1 + Ξ(r) = 1/D(r)
```

This scaling factor modifies electromagnetic fields in a gravitational environment.

---

## Maxwell Field Scaling

```
E'(r) = s(r) · E(r)
B'(r) = s(r) · B(r)
```

The fields are scaled by the same factor, preserving the E/B ratio and Maxwell's equations structure.

---

## Effective Refractive Index

```
n_eff(r) = s(r) = 1 + Ξ(r)
```

Gravity acts as an effective medium with refractive index s(r).

---

## Wave Equation

```
(1/s) ∂/∂r [(1/s) ∂E/∂r] - (1/c²) ∂²E/∂t² = 0
```

The modified wave equation includes the scaling factor. When transforming dρ = s(r)·dr:
- Include the chain-rule terms (s·s' contribution)
- Use analytic derivatives, NOT finite-difference for oscillatory fields

---

## Physical Distance

```
dρ = s(r) · dr
```

The physical (radar) distance dρ differs from coordinate distance dr by the scaling factor.

---

## Validation (45/45 PASS)

- GPS redshift: < 0.05% error
- Pound-Rebka: exact match
- Shapiro delay: 13/13 PASS (with PPN correction)
- Light deflection: matches Eddington 1.75"
- 13 astronomical objects consistent

**Tests:** `test_radial_scaling.py`
