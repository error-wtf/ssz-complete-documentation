# Lorentz Indeterminacy at v=0

**Paper:** 19 (Geometric Resolution of the Lorentz Indeterminacy at v=0)

---

## The GR Problem

```
γ_GR(v) = 1 / √(1 - v²/c²)

At v = 0: γ_GR = 1 (trivial)
```

The standard Lorentz factor at v=0 gives no information about the gravitational environment. A clock at rest in a gravitational field has γ=1 regardless of field strength — but it IS time-dilated.

---

## The SSZ Solution

```
γ_SSZ(v) = exp(Ξ · v²/c²)

At v = 0: γ_SSZ = exp(0) = 1
```

This is **regular** (no indeterminacy), and the gravitational encoding persists through the Ξ parameter even when v=0.

The segment density Ξ provides the "missing" gravitational information that the standard Lorentz factor cannot encode at zero velocity.

---

## Key Insight

In SSZ, the gravitational time dilation is encoded in Ξ itself, not in a velocity-dependent factor. The v=0 problem is resolved by construction: D(r) = 1/(1+Ξ(r)) works at all velocities including v=0.

**Test:** `test_lorentz_limit.py`
