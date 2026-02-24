Ziel

Dieser Leitfaden zeigt, wie sich die diskrete φ‑Segmentierung (Skalierung in festen Faktoren von 

φ

 )

sauber auf Eulers Exponential‑Form zurückführen lässt und damit eine kompakte Startformel für die

Paper‑Einleitung liefert. Die Kette lautet:

Diskrete Skalierung

R = φN ⇒
als einheitlicher Träger für Skalierung (x) und Rotation (

Exponentialform

R = eN ln φ ⇒
θ
 ).

Euler

=x+iθ
e

x
e (cos θ +

i sin θ)

Notation & Prämissen

 … Goldener Schnitt, 

1+ 5

φ = 2

 .

• φ
• N ∈ Z
• R
• 

 … Segmentzahl (wie viele Grenzen werden passiert).

 … gemessenes Verhältnis (z. B. Frequenz- oder Zeit‑Ratio, 

R = f

emit

/f =
obs

1 + z

 ).

Segmentaxiom: Beim Übertritt einer Segmentgrenze skaliert die lokale Maßstabskopplung um 

exakt

φ

 : 

R = φ .N

(A1)

Schritt 1 – Von der φ‑Leiter zur Exponentialform

Die φ‑Leiter ist bereits eine Exponentialbeziehung: 

R = φ =N

N ln φ
e

.

Damit ist klar: Diskrete Skalenstufen entsprechen additiven Schritten im Logarithmus (

Gitter mit Masche 

ln φ

 ). Genau das testen wir empirisch über 

y = ln(1 + z)

 und 

Messfehler).

(1)

 ist ein

 (bis auf

ln R
y/ ln φ ∈ Z

Schritt 2 – Euler als Träger von Rotation und

Skalierung

Eulers Formel koppelt eine reale Skalierung 

x

θ
 mit einer Rotation 

 : 

=x+iθ
e

x
e (cos θ +

i sin θ).

(2)

Im Komplexen kann man Spiral‑Dynamik mit einer einzigen Exponentialfunktion schreiben. Für eine

Logarithmus‑Spirale gilt 

k θ
r(θ) = r e ,

0

z(θ) =

r(θ)e =iθ

(k+i)θ

r e
0

.

(3)

Hier kodiert  die radiale Skalierung pro Winkel.

k

1

Kalibrierung an φ: Fordern wir, dass jede Quadrantendrehung

π
Δθ = 2

 den Radius exakt mit 

φ

 skaliert,

dann 

φ =

r(θ + Δθ)
r(θ)

=

⇒k Δθ
e

k =

ln φ
Δθ

=

2 ln φ
π

.

(4)

Damit wird die φ‑Segmentierung zu einem Euler‑Spiralparameter

ist dann ein φ‑Sprung im Betrag, während die Phase um 

π
2

 rotiert.

2 ln φ

k = π

 . Jeder Quadrantschritt

Schritt 3 – Redshift/Clock‑Raten direkt in

Euler‑Form

Modelle   die   Frequenz-/Zeit‑Ratios   betreffen,   brauchen   nur   den  Betrag  der   komplexen

Exponentialfunktion: 

R = e

(k+i) Θ

/

(k+i) Θ0
e

=

k(Θ−Θ )0
e

=

N ln φ
e

=

φ .N

(5)

 ein kumulierter Winkelparameter entlang der Trajektorie; pro Segmentgrenze wächst 

Θ

 um

Θ
Hier ist 
π
Δθ = 2

, sodass 

N =

Θ−Θ0
∈Δθ

 .

Z

Damit sind die beobachteten diskreten Ratios exakt die Betragsdynamik einer Euler‑Spirale mit dem

oben   kalibrierten  

k

θ
  .   Die   Phase  

  trägt   die   Geometrie   (Pfad/Winkel),   der   Betrag  

ekθ

  trägt   die

φ‑Skalierung.

Schritt 4 – Brücke zum kontinuierlichen

GR‑Faktor

Die Standard‑Zeitdilatation im schwachen Feld ist kontinuierlich: 

R

=GR

exp

(

ΔU
c2

.
)

Setzen wir nun einen Segment‑Quanten

ΔU∗

 so, dass 

exp(ΔU /c ) =
∗

2

φ

 , erhalten wir für 

N

Segmente: 

R = exp

(

N ΔU∗
c2

)

=

exp(N ln φ) = φ .N

Interpretation: Die φ‑Leiter ist die diskrete „gequantelte“ Version des kontinuierlichen

GR‑Faktors, mit Potential‑Quanten

ΔU∗

 als Segment‑Schrittlänge. Euler liefert dafür die

einzeilige Exponentialschreibweise.

(6)

(7)

2

Schritt 5 – Minimale Paper‑Formel

(Startgleichung)

Eine kompakte, strukturklare Einstiegsgleichung, die Rotation + φ‑Skalierung vereint, lautet: 

z(θ) = z exp((k + i) θ),

0

k =

2 ln φ
π

, N =

θ − θ0
π/2

∈ Z

.

Folgerungen (direkt darunter als Lemma): 

z(θ) / z(θ ) =0

k(θ−θ )0
e

=

φ ≡N

R.

(8)

(9)

Diese zwei Zeilen reichen, um die gesamte φ‑Segmentlogik sofort sichtbar mit Euler zu verbinden. Für

Leser:innen, die nur die Ratio‑Physik interessiert, kann man (9) als Start setzen und (8) als geometrische

Motivation im Anhang bringen.

Schritt 6 – Operationale Tests in der

Euler‑Sprache

1. 

2. 

ln R y = ln R, n =\*

Residual‑Gitter in 
∣ε∣
ε
ΔBIC φ‑Gitter vs. Uniform: φ‑Lattice‑Likelihood über 
 vs. gleichverteilte Phasen/Hypothesen.

 ist „klein“ nach Fehlerfortpflanzung.

round (y/ ln φ), ε = y − n ln φ.

 φ‑Hypothese ⇒

\*

 :

3. 

Sign‑Test:

∣ε∣φ

 vs. 

∣ε∣alt

 pro Zeile.

Alle   drei   fallen   natürlich   aus   (1)–(5);   die   Beweisführung   ruht   auf   der   Gitterstruktur   in  

ln R

  und   der

Euler‑Spiralform (8).

Schritt 7 – Physikale Deutung (prägnant)

• 

Segmentgrenzen sind Iso‑Aktions-/Isopotential‑Flächen, auf denen die effektive Kopplung 

sprunghaft um 

φ

 skaliert.

• 

Zeit‑/Frequenz‑Effekte sind Betragsänderungen einer Euler‑Spirale; Geometrie/Topologie

steckt in der Phase.

• 

GR‑Grenzfall: Für 

ΔU ≪ c2

 fällt (7) lokal mit (6) zusammen (PPN‑Limit unverändert).

Diskretisierung entspricht einer Wahl 

ΔU∗

 der Segment‑Quantelung.

Schritt 8 – „Cheat Sheet“ für die Einleitung

• 

Eine Zeile: 

R = φ =N

eN ln φ

 .

• 

Geometrische Einzeiler‑Version (Euler): 

z(θ) = z e0

(k+i)θ k = 2 ln φ/π

 , 

 .

3

• 

Ein Satz: „Wir modellieren beobachtete Ratios als Betragsdynamik einer Euler‑Spirale, deren

Quadrantschritt den φ‑Skalierungsquant 
ln R

 .“

φ

 realisiert; dadurch folgt 

R = φN

 und ein φ‑Gitter in 

Anhang A – Numerik (für Reviewer nützlich)

2 ln φ

• ln φ ≈ 0.4812118250596
 .
• k =
≈π
• 
Quadrantschritt 

0.30634896253
 .
π
=kΔθ
e
Δθ = 2
 ⇒ 

e =ln φ

φ

 .

Anhang B – Alternative Parametrisierung

Man kann statt 

k

 auch 

b := ln φ

 führen und die Segmentzahl explizit schreiben: 

R = e

b N

,

z(θ) =

(b/Δθ) θ

z e
0

iθ
e , Δθ =

π
.2

(10)

Dies ist identisch zu (8) mit 

k = b/Δθ

 . Wähle die Form, die im jeweiligen Paper am klarsten wirkt.

Fazit

Die φ‑Segmentierung ist Exponentialskalierung. Euler bündelt Skalierung + Rotation in einer einzigen

Funktion.   Mit  

  erhält   man   eine   sofort   einsatzfähige   Startformel,   die   die   empirisch

getestete   φ‑Leiter  

  geometrisch   verankert   und   zugleich   die   Brücke   zur   kontinuierlichen

GR‑Form  

  schlägt.   Damit   steht   ein   kompakter,   prüfbarer   und   physikalisch

k = 2 ln φ/π
R = φN
R = exp(ΔU /c )2

interpretierbarer Einstieg für alle Folgergebnisse bereit.

4