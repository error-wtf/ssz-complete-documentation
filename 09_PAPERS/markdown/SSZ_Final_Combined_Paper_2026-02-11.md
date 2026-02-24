## Segmented Spacetime (SSZ)

A phi-geometric extension of GR with segment density Xi, SSZ time dilation, and a no-free-parameters cosmology test scaffold

Authors:

Carmen Wrede · Lino Casu · Akira (AI collaborator)

Date:

2026-02-11

Status: consolidated paper (merges 'Finales Paper' + 'Drei Ausblicke' and includes reproducibility tests)

Abstract. Segmented Spacetime (SSZ) is a falsifiable, phi-motivated extension of General Relativity (GR) formulated via a dimensionless segment-density field Xi and an SSZ time-dilation factor D\_SSZ = 1/(1+Xi). SSZ is engineered to reproduce GR in the weak-field regime (g1) and to introduce controlled, saturating deviations in the strong-field regime (g2) without divergences. This paper consolidates the current SSZ axioms, regime definitions, and anti-circularity rules, and it adds a no-free-parameters cosmology scaffold that turns any proposed effective Xi(z) into immediate contradiction tests against (i) CMB acoustic-scale proxies, (ii) BBN expansion-rate proxies, and (iii linear growth of structure. We also provide an explicit reproducibility and regression-test report fo included reference implementation (ssz\_cosmo.py / run\_cosmo.py) and note one edge-case bug (z\_max=0) plus a minimal fix.

Keywords: segmented spacetime; strong-field gravity; time dilation; phi geometry; falsifiability; cosmology scaffold; CMB; BBN; growth of structure

## 1. Motivation and scope

SSZ is a phenomenological gravity extension designed to stay extremely close to GR in weak fields while remaining falsifiable in strong fields. The central design constraints are: (a) explicit axioms derived consequences, (b) no hidden free parameters per dataset, (c) regime clarity (g1 vs g2), and (d) reproducible computational predictions with residual-based validation rather than least-squares curve fitting.

This consolidated paper merges the core SSZ definitions (time dilation, segment density, saturation) with the practical next-step roadmap (fixing the regime transition r*, cosmological inhomogeneity tests, and an operational g1/g2 classifier), and it appends the current numeric test report for the minimal cosmology scaffold shipped in the accompanying code files.

## 2. SSZ axioms, definitions, and regimes

## 2.1 Segment-density field Xi

SSZ postulates a dimensionless scalar field Xi that represents an effective 'segmentation density' of spacetime. Xi is intended to be derived from regime formulas and fixed constants rather than tuned per object.

## 2.2 SSZ time dilation

SSZ defines a proper-time factor

## D\_SSZ(r) = 1 / (1 + Xi(r))

so that local proper time is d t = D\_SSZ dt. This is the primary SSZ input to redshift and clock-comparison observables.

## 2.3 Saturation (no divergence)

SSZ assumes Xi saturates in the strong field: Xi is bounded above by a theory-fixed maximum Xi\_max (often tied to the phi construction). This avoids singular divergences in D\_SSZ and provides a controlled strong-field limit.

## 3. Regime formulas and the g1/g2 bridge

## 3.1 Weak-field (g1): GR limit

In g1, SSZ uses a GR-matching segment density proxy such as Xi\_weak(r) = r\_s/(2r). For Xi &lt;&lt; 1, D\_SSZ » 1 - Xi, which matches GR behavior in the weak field to leading order.

## 3.2 Strong-field (g2): saturating segmentation

In g2, SSZ uses a saturating functional form (phi-motivated), e.g. Xi\_strong(r) = min(1 - exp(-phi r/r\_s), Xi\_max). This yields a finite horizon value (e.g. Xi(r\_s)=1-exp(-phi) » 0.8017) and a finite minimum dilation D\_min = 1/(1+Xi\_max).

## 3.3 Fixing the regime transition r*

A central 'no-free-parameters' requirement is that the regime transition r* is not a hand-chosen blending point. The recommended definition is an invariant equality condition (e.g. Xi\_weak(r*) = Xi\_strong(r*)) or an equivalent observable-level equality, solved once and then frozen globally.

## 4. Anti-circularity and no-free-parameters rules

SSZ commits to an explicit anti-circularity protocol: No free parameters per object: phi, Xi\_max, regime formulas, and transition logic are global. Matching points like r*: determined once by an invariant criterion, not per dataset. No least-squares fitting as core evidence: use exact algebra where possible; validate via residuals and consistency checks. Calibration vs validation separation: any calibration step must be declared and excluded from hold-out validation.

## 5. Cosmology extension as a minimal falsification scaffold

## 5.1 Principle

The cosmology module is intentionally minimal: it accepts any effective Xi(z) and evaluates immediate contradiction tests against three standard pillars: CMB acoustic-scale proxies, BBN expansion-rate proxies, and linear growth of structure. The module explicitly separates two time conventions for how D\_SSZ(z) maps into H(z).

## 5.2 Two time conventions (A/B)

With d t = D\_SSZ(z) dt, there are two consistent conventions depending on which time variable is taken as the cosmological 'clock':

```
Mode 'divide': H_SSZ = H_GR / D_SSZ = H_GR (1+Xi) Mode 'multiply': H_SSZ = H_GR · D_SSZ = H_GR / (1+Xi)
```

## 5.3 Minimal observables

The reference implementation computes: (i) a CMB acoustic-scale proxy via the sound horizon r\_s(z*) and angular diameter distance D\_A(z*), (ii) a BBN proxy via the ratio H\_SSZ/H\_GR at z » 4×10^9, and (iii) linear growth D(z) and f(z) via the standard growth ODE with E(z).

## 6. Three next steps (roadmap) - from the 'Drei Ausblicke' working paper

This roadmap is included to reduce attack surface and increase falsifiability: (1) r* fixation as a physics constraint: define r* by an invariant condition (weak = strong) and derive constraints from i (2) Cosmology as an inhomogeneity problem: treat SSZ signatures via a potential/lensing and runtime mapping rather than a homogeneous Xi(z) background. (3) g1/g2 operationalization: provide a deterministic regime classifier (indicators, thresholds, observable routing) with explicit hooks.

## 7. Reproducibility and regression-test report (this release)

## 7.1 Files in this bundle

The following files were tested together: ssz\_cosmo.py, run\_cosmo.py, ssz\_cosmo\_results\_divide.csv, ssz\_cosmo\_results\_multiply.csv, ssz\_cosmo\_summary\_all.json, and the two reference plots growth\_both.png and Hratio\_both.png.

## 7.2 Deterministic reproduction

Re-running the reference pipeline reproduces the provided CSV outputs to machine precision. Maximum absolute deviation (divide): 2.220e-16. Maximum absolute deviation (multiply): 1.110e-16. Identity checks (algebraic invariants): max |(Hratio\_div·Hratio\_mul) -1| = 2.220e-16; max |Hratio\_div 1/D| = 2.220e-16; max |Hratio\_mul -D| = 2.220e-16.

## 7.3 Summary metrics (CMB/BBN)

| Metric                 |    divide |   multiply |
|------------------------|-----------|------------|
| CMB theta_GR (rad)     | 11.3467   |  11.3467   |
| CMB theta_SSZ (rad)    | 11.3468   |  11.3467   |
| CMB theta ratio SSZ/GR |  1        |   0.999999 |
| CMB r_s ratio SSZ/GR   |  0.999988 |   1.00001  |
| CMB D_A ratio SSZ/GR   |  0.999988 |   1.00001  |
| BBN H ratio at z=4e9   |  1.00001  |   0.99999  |

## 7.4 Growth and H(z) ratios at benchmark redshifts

| Mode: divide   | Mode: divide   | Mode: divide   | Mode: divide   | Mode: divide   | Mode: divide   |
|----------------|----------------|----------------|----------------|----------------|----------------|
| z              | D_GR           | D_SSZ          | f_GR           | f_SSZ          | Hratio         |
| 0.0            | 1.000000       | 1.000000       | 0.263819       | 0.263816       | 1.000010       |
| 0.5            | 0.768876       | 0.768878       | 0.761267       | 0.761256       | 1.000012       |
| 1.0            | 0.606721       | 0.606726       | 0.876514       | 0.876501       | 1.000012       |
| 2.0            | 0.417160       | 0.417165       | 0.958186       | 0.958171       | 1.000013       |
| 5.0            | 0.211250       | 0.211255       | 0.993448       | 0.993433       | 1.000013       |
| 10.0           | 0.115406       | 0.115409       | 0.996863       | 0.996848       | 1.000013       |

| Mode: multiply   | Mode: multiply   | Mode: multiply   | Mode: multiply   | Mode: multiply   | Mode: multiply   |
|------------------|------------------|------------------|------------------|------------------|------------------|
| z                | D_GR             | D_SSZ            | f_GR             | f_SSZ            | Hratio           |
| 0.0              | 1.000000         | 1.000000         | 0.263819         | 0.263822         | 0.999990         |
| 0.5              | 0.768876         | 0.768873         | 0.761267         | 0.761277         | 0.999988         |
| 1.0              | 0.606721         | 0.606717         | 0.876514         | 0.876527         | 0.999988         |
| 2.0              | 0.417160         | 0.417155         | 0.958186         | 0.958200         | 0.999987         |
| 5.0              | 0.211250         | 0.211245         | 0.993448         | 0.993464         | 0.999987         |
| 10.0             | 0.115406         | 0.115403         | 0.996863         | 0.996878         | 0.999987         |

## 7.5 Reference plots

Figure 1 shows the linear growth factor D(z) for GR and SSZ under both time conventions. Figure 2 shows the ratio H\_SSZ/H\_GR under both conventions. Note: in Figure 2, the y-axis uses a small-offset notation; values slightly below 1 may appear as negative tick labels when plotted as (1 1e-5 offset).

## Linear growth factor (GR vs SSZ modes)

Z

Figure 1. Growth factor D(z): GR vs SSZ (divide and multiply).

<!-- image -->

Figure 2. Hubble ratio H\_SSZ/H\_GR: divide gives &gt;1 by O(1e-5), multiply gives &lt;1 by O(1e-5).

<!-- image -->

## 8. Known issues and minimal fixes

## 8.1 Edge case: Xi\_cosmo when z\_max = 0

When Xi(z) is generated from a normalized (1+z)/(1+z\_max) form, calling Xi\_cosmo on a single-point array z=[0] yields z\_max=0 and currently returns Xi=1 and D\_SSZ=0.5. This does not affect the shipped CSV benchmarks (which evaluate multiple z values at once), but it can break single-point queries and unit tests. Observed: Xi\_cosmo([0])=1, D\_SSZ([0])=0.5. Recommended fix: if z\_max==0, return Phi0 for all entries.

## 8.2 Notation caution: acoustic-scale definition

The current implementation computes a CMB 'theta' proxy using r\_s(z*) and D\_A(z*). In cosmology literature, theta\_* is often defined as r\_s/D\_M (or equivalently r\_s/[(1+z*)D\_A]). For SSZ/GR ratio tests this distinction mostly cancels, but for absolute comparison to Planck-style numbers the definition should be stated explicitly.

## 9. Reproducibility instructions

To reproduce the cosmology scaffold outputs:

- 1) Ensure Python 3 with numpy/pandas installed.
- 2) Run:

python run\_cosmo.py

This produces two CSV files and a combined JSON summary for both coupling modes. The included regression checks in Section 7 confirm that the current bundle is deterministic to machine precision.

## 10. Conclusion

This consolidated document provides a single coherent SSZ paper that covers: axioms and regimes (g1/g2), anti-circularity rules, the three-step roadmap to reduce scientific attack surface, and a te no-free-parameters cosmology scaffold with reproducibility evidence. The next work should prioritize (i) a physics-fixed r* criterion, (ii) explicit inhomogeneity-based cosmology signatures (CMB lensing ISW), and (iii) a deterministic regime classifier that routes each observable through the correct SSZ regime without tuning.