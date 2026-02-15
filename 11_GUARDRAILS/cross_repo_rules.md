# Cross-Repository Rules

---

## The Core Problem

"Apparent contradictions" between repos arise from **missing documentation**, not faulty physics. Each repo is internally consistent but may use different scopes, methods, or regime ranges.

---

## Repo Scope Index

| Repo | Scope | Ξ Formula | PPN? |
|------|-------|-----------|------|
| ssz-qubits | Weak | r_s/(2r) | NO |
| ssz-metric-pure | Strong | 1-exp(-φr_s/r) | YES |
| maxwell/lensing | Blend | Hermite C² | YES |
| Unified-Results | Strong | Ξ_max(1-exp(...)) | YES |
| frequency-curvature | Weak+PPN | r_s/(2r) | YES |

---

## Rules

1. **ALWAYS** classify the observable before calculating
2. **NEVER** compare repos without checking their scope
3. **50%** of GR for null observables is **NOT A BUG** (Ξ-only vs PPN)

---

## False Alarm Detection

| Symptom | Actual Cause |
|---------|-------------|
| 50% of GR result | Ξ-only instead of PPN |
| Formulas look different | Different scope/regime |
| Tests contradict each other | Different observables |
| Different r*/r_s values | Different Ξ forms (1.595 vs 1.387) |

---

## Deprecated Formula Handling

| Where Found | Action |
|-------------|--------|
| Active calculation path | **REPLACE** immediately |
| Notes/old code only | Mark as deprecated, don't patch |

---

## Key Insight

> **Guardrails = Documentation hardening, NOT error correction.**
>
> The repos are physically correct and internally consistent.
> Guardrails prevent cross-repo misunderstandings.
