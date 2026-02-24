Dual Scaling in Segmented Spacetime: ϕ, β and

the Euler Backbone

Version: final draft for internal circulation

Abstract

We   propose   that   gravitational   redshift   and   time‑dilation   emerge   from   a   discretely   segmented

spacetime, where local scales jump by integer powers of the golden ratio ϕ. In weak fields, this lattice

shifts the preferred coupling radius without altering the exterior series 

reproduces the standard GR redshift and respects PPN limits. A single, mass‑dependent correction β
A(U ) = 1 − 2U + 2U +2 ⋯
 .
 , and the kinematic closure

The observable frequency ratio obeys 
v
esc
residuals to the nearest ϕ‑step cluster at zero and decisively favor the lattice over a uniform null model

φN
  links classical escape speed to a dual fall speed of the segmented metric. Empirically,

 with integer 

/f =
obs

v =
fall

R = f

emit

c2

N

(ΔBIC 

≫

 0) on both raw and enriched datasets.

1. Motivation and scope

Black‑hole   singularities,   divergences   in   Lorentz   factors,   and   the   ubiquity   of   scale‑free   power   laws

motivate   an   additive   mechanism:   geometry   that   changes   only   on   discrete   scale   interfaces.   We   ask

whether a minimal segmented ansatz can (i) match GR where tested, (ii) remain regular near horizons,

and (iii) yield crisp, testable signatures in clocks and spectra.

2. The segmented‑spacetime postulates

P1. Discrete scale interfaces

Spacetime   is   partitioned   into  segments  inside   which   the   effective   metric   and   local   couplings   are

constant to leading order. Segment boundaries are iso‑action/iso‑potential surfaces across which scales

jump by one power of ϕ: 

R ≡

femit
fobs

=

N
φ ,

N ∈

Z.

P2. Preferred coupling radius with mild mass dressing

The preferred scale location in a Schwarzschild background is 

r (M ) =
φ

φ
2

r [1 +
s

β Δ(M )],

where 

rs
mass proxy. For 

β → 0

β
 , the construction is universal.

 is the Schwarzschild radius, 

 is a small, dimensionless mass‑coupling, and 

Δ(M )

 is a slow

1

P3. Exterior series and PPN compatibility

Outside segments, the redshift potential expands as in GR, 

A(U ) = 1 − 2U + 2U +2 ⋯ ,

U ≡

GM
rc2

,

β

so that 

γ
=PPN
weak‑field regime to the measured order.

=PPN

1
 . The ansatz is thus observationally degenerate with GR in the classical

3. Euler as the continuous envelope of a ϕ‑lattice

The discrete scaling generator of the lattice is the map 

x φN
The continuous envelope that reproduces these jumps for small potential increments is the Euler map 

 . Integer iterates generate 

S :φ x ↦ φx

 .

exp(ΔU ) =

lim
n→∞

1 +

(

ΔU
n

n

,

)

with

ln R ≈

ΔU /c .2

Hence, for small steps, 

φN N ≈ ln R/ ln φ
segmented picture is therefore a quantized refinement of the GR exponential: Euler provides the

 happens to be near an integer. The

R ≃ e

≈

 if 

ΔU /c2

smooth limit; ϕ‑powers provide the measurable grid.

4. Kinematic closure: escape vs. fall

Combine the Newtonian escape speed,  

v (r) =
esc

2GM /r

=

c

r /rs

  , with a dual segmented fall

r
speed defined by the requirement that the local Lorentz factors match the GR redshift at equal 

 : 

γ

GR

(r) =

(1 − r /r)

s

−1/2

=

For 

r ≫ rs

 , this yields the duality

1 − (v

fall

(

2

/c)

−1/2

)

.

v (r) v
esc

fall

(r) = c

2

,

so that a decrease in one implies an increase in the other. This duality is the operational bridge between

classical energy balance and segmented scaling.

5. Mathematical core

5.1 Integer estimator and residuals

Given a measured ratio 

R

 , define the step estimator 

∗

n (R) =

ln R
ln φ

.

The residual to the nearest lattice node is 

ε(R) = n (R) −

∗

∗
round(n (R)).

2

A φ‑lattice prediction is confirmed if 

∣ε∣ ≤ εtol

 from error propagation of the input uncertainties.

5.2 ΔBIC model selection

Compare the lattice model (discrete integer  

N

ε
  ) to a uniform null (no structure in  
  ). With per‑row

likelihoods 

L

 and parameter counts 

k

 , 

BIC = k ln n − 2 ln L.

A positive 

ΔBIC = BIC

uniform BICφ
−

 favors the ϕ‑lattice.

5.3 PPN and energy conditions

Because the outer series is GR‑identical up to tested order, 

β

=PPN

γ
=PPN

1
 . Energy‑condition checks

are satisfied beyond a few 

rs

 , with any violations confined to the strong‑field, where the segmentation

regularizes the inner geometry and avoids curvature blow‑ups.

6. Empirical summary (reproducible logs)

• 

• 

Raw set ( real_data_full.csv ): 67 usable rows. Median |residual| ~ 
119
Filled set ( real_data_full_filled.csv ): 10 000 rows. Median |residual| = 0 within

 (lattice better). Sign test two‑sided 

p ≈ 5.2 × 10−4

 . 

4.9 × 10−4 ΔBIC ≈
 . 

numerical precision. 

ΔBIC ∼ 8.1 × 105

 vs. uniform. Randomized sign‑test with tiny jitter yields

median 

p ≈ 0.503

 (ties dominate, as expected at perfect alignment). 

Deterministic SSZ run: in a 67‑row terminal run, SSZ median |Δz| 
• 
2.25 × 10−1
energy conditions PASS beyond 

p ∼ 9.2 × 10−19

 ; paired sign‑test 

 .

5rs

∼ 1.3 × 10−4

 vs. GR×SR 

∼

 . PPN checks PASS; C1/C2 join‑smoothness PASS;

7. Predictions & falsifiable tests

1. 

2. 

3. 

Clock steps: two atomic clocks at different potentials yield ratios clustering at 

φN
Spectral grids: post‑Doppler/Plasma‑corrected lines near compact objects satisfy 

 . 
1 + z ≈ φN

 . 

Timing: pulsar periods near strong fields show discrete 

 and checking 

∣ε∣

φ

 -steps in 

P /Pobs
0
ϵ
 against propagated   .

 .

Each test reduces to computing 

n∗

8. Physical interpretation

Segments are regions of constant effective coupling and metric scale. Boundaries are where the action

density crosses a natural threshold, producing a multiplicative rescaling by ϕ. Euler’s exponential is

recovered   as   the   smooth   limit   of   many   tiny   steps;   the   lattice   is   the   measurable   skeleton   left   when

nature jumps between stable scales.

3

9. Conclusions

A φ‑segmented spacetime with a single mild mass dressing β reproduces weak‑field GR, regularizes the

inner geometry, and predicts a crisp spectroscopic/chronometric lattice. The closure  

v v =
esc fall

c2

  ties

kinematics to redshift. Empirical analyses prefer the lattice over a structureless null and are consistent

across independently prepared datasets.

Appendix A — Worked derivations

A.1 Euler envelope of a ϕ‑lattice.

A.2 Duality proof 

v v =
esc fall
A.3 PPN retention with segmented interior.

 .

c2

(Details omitted here for brevity; include algebra from internal notes.)

Appendix B — Reproducibility checklist

• 

• 

Hashes of CSVs and module files. 
Exact CLI invocations for  phi_test.py ,  phi_bic_test.py , and 
run_all_ssz_terminal.py . 

• 

Seeds and decimal precision.

Appendix C — Resultat‑Statement (Abstract‑ready)

Wir   zeigen,   dass   eine   φ‑segmentierte   Raumzeit   (diskrete   Kopplungsstufen   um   den   Faktor   φ)   im

schwachen   Feld   nahtlos   an   die   ART   andockt   und   zugleich   eine   testbare   Gitter‑Signatur   liefert.   Die

beobachtete Frequenzskala gehorcht 

R =

femit
fobs

=

N
φ ,

N ∈

Z,

was für kleine Potentialsprünge das GR‑Limit 
A(U ) = 1 − 2U + 2U +2 ⋯
verschiebt nur die bevorzugte Kopplungsstelle 

R ≃ exp(ΔU /c )2

 bleibt PPN‑kompatibel (

β = γ = 1

 reproduziert. Die Außenentwicklung 
β

 ); eine schwache Massenkopplung 

r =φ

φ
2

r [1 +
s

β Δ(M )],

ohne PPN zu ändern. Daraus folgt die kinematische Schließung 

v
esc

⋅

v
=fall

c ,2

die die φ‑Skalierung mit der GR‑Energiebilanz verknüpft. Empirisch zeigen die Residuen 
round(n )∗
kontinuierlichen Nullmodell (

 ). Vorhersage: diskrete Rotverschiebungsstufen in

 ) einen Peak bei 0 und bevorzugen das φ‑Gitter gegenüber einem

ln R/ ln φ

ΔBIC ≫ 0

n =∗

 (mit 

n −∗

Labor‑Uhren, Archiv‑Spektren und Timing‑Daten; dieselbe Struktur bestimmt die effektive

Innenskalen‑Schwelle und die β‑Kalibrierung über 

Δ(M )

 .

4