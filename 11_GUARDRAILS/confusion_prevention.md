# Confusion Prevention Strategy

**Status:** CANONICAL

---

## Three-Layer Strategy

### Layer 1: Repo Scope Index
Every repo has a documented scope (see `cross_repo_rules.md`). Before using results from a repo, check its scope.

### Layer 2: Method Assignment
Every observable has a documented method (see `method_assignment.md`). Before calculating, check the method.

### Layer 3: False Alarm Recognition
Known patterns that look like errors but are design features:

---

## Common False Alarms

### 1. "Lensing is 50% too low!"
**Pattern:** Computing lensing with Ξ-only gives α = r_s/b instead of 2r_s/b
**Reality:** Ξ-only captures g_tt only. PPN (1+γ) gives the full result.
**Fix:** Use PPN method for null observables.

### 2. "Two different r* values!"
**Pattern:** r*/r_s = 1.595 in one place, 1.387 in another
**Reality:** Different Ξ formulas have different GR intersection points:
- 1.595: Ξ_weak ∩ D_GR
- 1.387: Ξ_strong ∩ D_GR
**Fix:** Identify which Ξ form is being used.

### 3. "Ξ values don't match between repos!"
**Pattern:** ssz-qubits gives Ξ=0.167 at r/r_s=3, ssz-metric-pure gives Ξ=0.259
**Reality:** qubits uses Ξ_weak, metric-pure uses Ξ_strong
**Fix:** Check repo scope before comparing.

### 4. "D_SSZ ≠ D_GR everywhere!"
**Pattern:** SSZ and GR time dilation differ at r/r_s < 10
**Reality:** This is the ENTIRE POINT of SSZ. They converge in weak field, diverge in strong field.
**Fix:** Not a bug. This is the prediction.

### 5. "Energy is not conserved!"
**Pattern:** Adding SR + GR + extra energies gives wrong total
**Reality:** Energy accounting must be multiplicative, not additive
**Fix:** Use E_obs = E_rest × (transform factors)

---

## Prevention Checklist

Before reporting a discrepancy:

- [ ] Checked repo scope? (weak/strong/full)
- [ ] Checked method assignment? (Ξ vs PPN)
- [ ] Checked regime? (r/r_s value)
- [ ] Checked for deprecated formula?
- [ ] Checked if it's a known false alarm pattern?

If all checks pass and the discrepancy persists → it's a real issue.

---

© 2025–2026 Carmen N. Wrede, Lino P. Casu
