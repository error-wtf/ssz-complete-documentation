# **SSZ: Drei nächste Schritte als eigenständiges** **Arbeits‑Paper**

### **r*‑Bestimmung, kosmologische Inhomogenitäts‑Tests, g1/** **g2‑Operationalisierung**

**Autoren:** Carmen Wrede · Lino Casu · Akira (AI‑Collaborator)


**Version:** Draft v0.9


**Datum:** 2026‑02‑11

### **Abstract**


Dieses Arbeits‑Paper operationalisiert drei konkrete nächste Schritte für **Segmented Spacetime (SSZ)**,
die unmittelbar die wissenschaftliche Angreifbarkeit reduzieren und die Falsifizierbarkeit erhöhen:


1) **Physikalische Fixierung des Regime‑Übergangs** _r_ \* (kein frei wählbarer Blend‑Punkt): Definition

über eine invariantenbedingte Gleichung (weak=strong) und daraus abgeleitete Constraints.


2) **Kosmologische Tests als Inhomogenitäts‑Problem** statt als homogener Ξ( _z_ )-Hintergrund:

Formulierung von Signaturen in CMB‑Lensing, ISW, BAO, und SNe‑Distanzen über eine SSZ‑Potential‑
und Laufzeit‑Abbildung, ohne Curve‑Fitting.


3) **g1/g2‑Operationalisierung** als klarer Algorithmus (Regime‑Klassifikator) mit deterministischen
Schwellen/Indikatoren und Test‑Hooks für jede Observable.


Ziel ist ein „no‑free‑parameters“-Pfad: Alle neuen Größen müssen entweder (i) aus SSZ‑Axiomen folgen
oder (ii) als globale, einmal fixierte Konstante mit anschließendem Hold‑out‑Test auftreten.

### **1. Minimaler SSZ‑Kern**


SSZ nutzt als Basiseingang die Segmentdichte Ξ und die Zeitdilatation


1

_D_ SSZ( _r_ ) = .
1 + Ξ( _r_ )


Zwei Regime:


   - Weak‑Field (g1):


1 _rs_
Ξweak( _r_ ) = .
2 _r_


1


   - Strong‑Field (g2), saturierend:


Ξstrong( _r_ ) = _ξ_ max(1 − _e_               - _ϕ r_ / _rs_ ), _ξ_ max = 1 − _e_               - _ϕ_ .


Die _Bridge_ ist erlaubt, aber **nicht als frei wählbare Story‑Glättung** .

## 2. Schritt 1: Physikalische Fixierung von r \*


**2.1 Problem**


Ein Blend‑Punkt _r_ \* darf nicht als „frei wählbar“ erscheinen. Er muss aus einer invarianten Bedingung

folgen.


**2.2 Invariante Definition**


Definiere _r_ \* als Lösung der Gleichheit


Ξweak( _r_ \*) = Ξstrong( _r_ \*) .


Also



1 _rs_ =
2 _r_ \*



_rs_ = _ξ_ max 1 − _e_ - _ϕ r_ \*/ _rs_ .

_r_ ( )



_r_ \*



Mit _x_ ≡ _r_ \*/ _rs_ :



1 - _ϕx_

= _ξ_ max(1 − _e_ ) .
2 _x_


_x_
_rs_ ), keine per‑Objekt‑Wahl.



1 - _ϕx_

= _ξ_ max(1 − _e_ ) .



Diese Gleichung ist **numerisch eindeutig** lösbar (monoton in für sinnvolle Parameter). Das Ergebnis _x_



ist eine **globale Konstante** (in Einheiten _rs_ ), keine per‑Objekt‑Wahl.



**2.3 Korrektheitskriterien**



1) **Eindeutigkeit:** Es darf nur eine physikalisch sinnvolle Lösung _x_ - 1 geben. 2) **Robustheit:** Kleine

numerische Perturbationen (Integrationsschritt, Float‑Precision) dürfen nicht signifikant verschieben. _x_



_x_ - 1



_x_
_r_ ≫ _r_ \* gilt Ξ ≈Ξweak, für _r_ ≪ _r_ \* gilt Ξ ≈Ξstrong



3) **Regime‑Semantik:** Für _r_ ≫ _r_ \* gilt Ξ ≈Ξweak, für _r_ ≪ _r_ \* gilt Ξ ≈Ξstrong.



**2.4 Bridge‑Gewicht ohne neue Freiheitsgrade**


Wenn _r_ \* fix ist, darf die Blend‑Form _w_ ( _r_ ) nur feste Exponenten nutzen, z. B.



1
4



_w_ ( _r_ ) = 4 .
1 + ( _rr_ \* )



_r_

\* )



Die „4“ ist hier nicht Fit, sondern eine **SSZ‑Grundzahl** (Segmentierungsbasis) und bleibt global fest.


**2.5 Testplan**


    - **Unit‑Test:** löse und prüfe residual _x_ ∣Ξweak −Ξstrong [∣] < Toleranz.


2


    - **Regression:** _x_ darf sich über Code‑Versionen nicht ändern (sonst Breaking Change).

    - **Observable‑Stabilität:** Variation von Blend‑Glättung (C¹ vs C²) darf Observables nur im

numerischen Fehlerband verändern.

### **3. Schritt 2: Kosmologie als Inhomogenitäts‑Signatur**


**3.1 Motivation**


Die homogene Abbildung Ξ( _z_ ) ist durch CMB/BBN extrem eingeschränkt. Daher muss SSZ‑Kosmologie

primär über **inhomogene Potentiale** wirken.


**3.2 SSZ‑Potential‑Mapping**


Wir benötigen eine konsistente Abbildung zwischen GR‑Potential Φ und SSZ‑Effekt (z. B. Laufzeit,
Redshift, Lensing).


Minimal‑Ansatz über einen effektiven Potentialfaktor F :


ΦSSZ( _r_ ) = F(Ξ( _r_ )) ΦGR( _r_ )


mit einer **theorie‑fixierten** Wahl, z. B.


1

F(Ξ) = 1 + Ξ oder F(Ξ) = = 1 + Ξ .
_D_ SSZ


Wichtig: Nur eine Definition, global fixiert.


**3.3 CMB‑Lensing als Primärtest**


CMB‑Lensing ist sensitiv auf die integrierte Potentialstruktur entlang der Sichtlinie:



_χ_ ∗



_χ_ ∗ - _χ_ (Φ + Ψ)



∗ _χ_ ∗          - _χ_

_φ_ ( _n_ ^) ∝ _dχ_ (Φ +
∫ _χ_ _χ_



0



_χ_ ∗ _χ_



(im GR‑Standard ohne Anisotropiestress Φ ≈Ψ).



Φ →ΦSSZ durch F(Ξ)
_CLφφ_ .



SSZ‑Testidee: Ersetze Φ →ΦSSZ durch F(Ξ). Das liefert deterministisch eine Vorhersage für das
Lensing‑Potential‑Spektrum _C_ _φφ_ .



_φφ_



**No‑fit‑Regel:** Nur die bereits aus Daten bekannten Dichtefelder (ΛCDM‑Matter) werden genutzt; SSZ
fügt nur F(Ξ( _r_ )) hinzu.


**3.4 ISW‑Effekt als Sekundärtest**


Der integrierte Sachs‑Wolfe‑Effekt misst zeitliche Potentialänderungen:



Δ _T_

_T_ )



ISW



Δ _T_

∝
( _T_



_d_

_dη_ (Φ + Ψ)
∫ _dη_



SSZ modifiziert die Potentiale über F(Ξ) und kann so ISW‑Cross‑Correlations (CMB×LSS) beeinflussen.


3


**3.5 BAO und SNe als Laufzeit‑Checks**


BAO und SNe testen Distanzen (Radial/Transversal):



_z_



_dz_ [′]
_H_ ( _z_ )′



_dz_

_DM_ ( _z_ ) = _c_ ∫ _H_ ( _z_ )′, _DL_ ( _z_ ) =



0



_L_ ( _z_ ) = (1 + _z_ ) _DM_ ( _z_ ).



Wenn SSZ primär inhomogen wirkt, muss die Hintergrund‑Distanzrelation GR‑like bleiben, aber SSZ
kann als **line‑of‑sight delay/lensing scatter** auftreten (Breiten/Skewness der Residuen, nicht als
Mittelwert‑Shift).


**3.6 Minimaler Daten‑Stack ohne Fit**




- Planck CMB Lensing _CL_



Planck CMB Lensing



_φφ_









ISW‑Cross‑Correlation (z. B. mit großen LSS‑Katalogen)
BAO‑Distanzen (BOSS/eBOSS/DR‑Kompilation)
Pantheon‑ähnliche SNe‑Hubble‑Residuals (nicht als neue Fit‑Kosmologie, sondern als Scatter‑/
Skew‑Test)



**Erfolgskriterium:** SSZ darf keine systematische Verschlechterung erzwingen; wenn es Verbesserung
gibt, muss sie ohne neue Parameter auftreten.

### **4. Schritt 3: g1/g2‑Operationalisierung als Algorithmus**


**4.1 Problem**


„g1 vs g2“ darf nicht ein narrativer Label sein, sondern muss als deterministische Klassifikation
implementiert werden.


**4.2 Regime‑Indikator**


Definiere einen dimensionslosen Feldstärke‑Indikator



und eine Segmentdichte‑Schwelle


Dann:



_rs_

_κ_ ( _r_ ) =
_r_


Ξth = Ξ( _r_ \*) .




- g1, wenn Ξ( _r_ ) < Ξth

- g2, wenn Ξ( _r_ ) ≥Ξth



Alternativ (wenn Ξ aus Datenfeldern kommt): - g1, wenn _κ_ < _κ_ ∗ - g2, wenn _κ_ ≥ _κ_ ∗



wobei _κ_ ∗ ≡ _rs_ / _r_ ∗ aus Schritt 1 folgt.



4


**4.3 Observable‑Router**


Jede Observable erhält eine Routing‑Regel:




- Time dilation / redshift: benutze _D_ SSZ(Ξ) in beiden Regimen, aber mit Ξ = Ξweak
Ξ = Ξstrong (g2) bzw. Bridged.



Time dilation / redshift: benutze _D_ SSZ(Ξ) in beiden Regimen, aber mit Ξ = Ξweak (g1) bzw.



(g2) bzw. Bridged.




- Lensing / Shapiro: benutze ΦSSZ = F(Ξ)ΦGR und entscheide, ob lokale g2‑Zonen dominant



sind (Cluster/NS/BH) oder ob g1‑Hintergrund genügt.


   - Cosmology: Hintergrund bleibt g1‑dominiert; g2 erscheint als inhomogene Korrektur in

Potentialintegralen.


**4.4 Testplan**


    - **Classifier‑Tests:** künstliche Inputs und _r_ _M_ müssen deterministisch g1/g2 liefern.




- **Edge‑Case:** _r_ ≈ _r_ ∗




**Edge‑Case:** _r_ ≈ _r_ ∗ muss stabil (keine Flip‑Flop‑Numerik).



**Observable‑Consistency:** identische Inputdaten dürfen nicht je nach Codepfad
widersprüchliche Outputs liefern.


### **5. Repro‑Protokoll**

Für jeden der drei Schritte gilt:


1) **Definitionen** **zuerst** (Formeln, Schwellen, Zeitkonvention). 2) **Code‑Implementierung**
(deterministisch, ohne Fit). 3) **Unit‑Tests** (lokal, schnell). 4) **Dataset‑Tests** (CMB/BBN/Growth oder
Lensing/ISW/BAO/SNe). 5) **Fail‑Fast** : Wenn ein Check scheitert, wird nicht „erklärt“, sondern die
Hypothese verworfen oder präzisiert.

### **Appendix A: To‑Do als konkrete Deliverables**


**A1 Deliverable für Schritt 1**




- Datei: `rstar_solver.py`

- Output: _x_ = _r_ ∗/ _rs_, _[κ]_ ∗, [Ξ] th

- Test:



Output: _x_ = _r_ ∗/ _rs_, _[κ]_ ∗,



Test: `test_rstar_equation.py`



**A2 Deliverable für Schritt 2**


    - Datei: `ssz_lensing_mapping.py`




- Input: Matter‑Potential aus Standard‑Pipeline, plus F(Ξ)

- Output: _CLφφ_ Ratio zu GR



Input: Matter‑Potential aus Standard‑Pipeline, plus
Output: _C_ _φφ_ Ratio zu GR



_φφ_



Test: sanity (ratio→1 bei Ξ →0)




- Test: sanity (ratio→1 bei Ξ →0)



**A3 Deliverable für Schritt 3**


5


   - Tests: deterministische Klassifikation + Randfälle


_Ende des Arbeits‑Papers._


6


