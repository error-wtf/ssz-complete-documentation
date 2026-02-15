# Kinematic Closure

**Paper:** 07 (Kinematische Schließung: Escape vs Fall)

---

## The Closure Relation

```
v_esc(r) × v_fall(r) = c²
```

### Explicit Proof
```
v_esc = c√(r_s/r)
v_fall = c√(r/r_s)

v_esc × v_fall = c² · √(r_s/r) · √(r/r_s)
              = c² · √(r_s · r / (r · r_s))
              = c² · √1
              = c²  ✓
```

### Properties
- **Mass-independent:** No M appears in the closure relation
- **Purely geometric:** Follows from the definition of r_s
- **Universal:** Holds at all radii, all masses
- **Exact:** No approximations involved

---

## Implications

1. Escape and fall velocities are **reciprocally linked** through c²
2. At r = r_s: both velocities equal c
3. Below r_s: v_esc > c but v_fall < c (the product remains c²)
4. Provides a kinematic constraint independent of the Ξ formulation

**Test:** `test_kinematic_closure.py`
