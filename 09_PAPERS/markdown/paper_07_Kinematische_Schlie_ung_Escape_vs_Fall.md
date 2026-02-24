# Paper 06: Von Ï†-Segmentierung zu Euler

## Bibliografische Daten
- **Titel:** Von Ï†-Segmentierung zu Euler: Beweiskette & Ableitung
- **Autoren:** Carmen N. Wrede, Lino P. Casu
- **Thema:** Mathematische Herleitung Ï† â†’ Euler

---

## Zusammenfassung

Dieses Paper zeigt, wie das Ï†-Segmentgitter auf die Euler-Darstellung zurückgeführt werden kann. Die Ï†-Logik ist eine Euler-Logik: Diskrete Skalenjumps sind die reelle Exponential-Komponente, Segment-Grenzrotationen die imaginäre.

---

## Axiome

### A1: Segment-Postulat
Raumzeit besitzt Diskretstufen S_n mit konstanter lokaler Kopplung und konstanter effektiver Metrik innerhalb eines Segments.

### A2: Skalenfaktor
Beim Ãœbergang S_n â†’ S_{n+1} skaliert jede relevante GröÃŸe durch den festen Faktor Ï†.
- Wellenlänge: Î» â†’ Ï†Î»
- Frequenz: f â†’ f/Ï†

### A3: Winkel-Quantelung
Die Segmentgrenze entspricht einer festen Phasenrotation Î”Î¸ (z.B. Ï€/2).

---

## Formeln

### Formel 1: Rotverschiebungs-Gitter

```
R â‰¡ f_emit/f_obs = 1 + z = Ï†^N,  N âˆˆ â„¤
```

**Erklärung:**
- Frequenzverhältnisse sind ganzzahlige Potenzen von Ï†
- Fundamentale Vorhersage des SSZ-Frameworks

---

### Formel 2: Logarithmisches Gitter

```
ln R = N ln Ï†
```

**Folgerung:** ln(1+z) ist periodisch modulo ln Ï†

---

### Formel 3: Ganzzahl-Schätzer

```
n* = round(ln R / ln Ï†)
```

**Residuum:**
```
Îµ = ln R / ln Ï† - n*  âˆˆ (-1/2, 1/2]
```

---

### Formel 4: Euler-Einbettung (ZENTRAL!)

```
z_k = râ‚€ · e^{k(ln Ï† + iÎ”Î¸)}
```

**Komponenten:**
- Magnitude: e^{k ln Ï†} = Ï†^k (Skalen-Jump)
- Phase: e^{ikÎ”Î¸} (Rotation)

---

### Formel 5: Logarithmische Spirale

```
r(Î¸) = râ‚€ · e^{bÎ¸}
b = ln Ï† / Î”Î¸
```

Für Viertelkreis (Î”Î¸ = Ï€/2):
```
b = 2 ln Ï† / Ï€ â‰ˆ 0.306
```

---

### Formel 6: Gruppenhomomorphismus

```
n â†¦ R = Ï†^n  ist Homomorphismus (â„¤, +) â†’ (â„âº, ·)
```

**Bedeutung:** Additive Segmentzahl â†’ Multiplikative Skalierung

---

### Formel 7: Euler-Zerlegung

```
e^{x+iθ} = e^x(cos θ + i sin θ)
```

Mit x = n ln Ï†:
- Realteil: Ï†^n cos(nÎ”Î¸) â†’ Amplitude
- Imaginärteil: Ï†^n sin(nÎ”Î¸) â†’ Phase

---

## Beweiskette (Skizze)

1. **Lemma 1:** n â†¦ Ï†^n ist Gruppenhomomorphismus
2. **Lemma 2:** âˆƒ Î”Î¸ > 0 mit z_n = râ‚€ e^{n(ln Ï† + iÎ”Î¸)} und |z_n| = Ï†^n
3. **Satz 2:** H_Ï† äquivalent zu Euler-Bahn auf log-Gitter
4. **Korollar:** ln(1+z) âˆˆ (ln Ï†)â„¤ bis auf Messfehler

---

## Testbare Vorhersagen

### 1. Ganzzahltest
```
n* = round(ln R / ln Ï†) mit kleinem |Îµ|
```

### 2. Î”BIC-Modellvergleich
```
Î”BIC = BIC_uniform - BIC_Ï† > 0 â†’ Ï†-Gitter bevorzugt
```

### 3. Periodizität
Histogramm von ε:
- Flach unter Nullhypothese
- Peak bei 0 unter H_Ï†

---

## Physikalische Interpretation

### Warum Euler?

1. **Kontinuierlicher Grenzwert** von diskreten Ï†-Sprüngen
2. **Komplexe Darstellung** vereint Skala und Rotation
3. **Logarithmische Spirale** als natürliche Geometrie

### Ï† vs. e

| Eigenschaft | Ï† | e |
|-------------|---|---|
| Diskret | Ja | Limit |
| Skala | Ï†^n | e^x |
| Geometrie | Segmente | Spirale |

---

*Erstellt: 2025-12-28*
