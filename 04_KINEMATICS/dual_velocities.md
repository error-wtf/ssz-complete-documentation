# Dual Velocities: Escape vs Fall

**Paper:** 02 (Dual Velocities in Segmented Spacetime)

---

## Definitions

```
v_esc(r) = c · √(r_s / r)     Escape velocity
v_fall(r) = c · √(r / r_s)    Fall velocity
```

---

## The Fundamental Invariant

```
v_esc(r) × v_fall(r) = c²     for ALL r
```

This is:
- **Independent of mass M** — purely geometric
- Equivalent to: √(2GM/r) × √(rc²/2GM) = c
- A SSZ-specific symmetry relating escape and infall

---

## Physical Interpretation

| Property | v_esc | v_fall |
|----------|-------|--------|
| At r → ∞ | 0 | ∞ |
| At r = r_s | c | c |
| At r < r_s | > c | < c |
| Relationship | Classical escape | Reciprocal velocity |

The duality means: knowing one velocity at any radius immediately determines the other.

---

## Connection to Redshift

```
v_fall / c = √(r/r_s) = √(1/2Ξ_weak)
```

In the weak field, v_fall encodes the gravitational redshift information.

**Tests:** `test_vfall_duality.py`, `test_dual_velocity.py`
