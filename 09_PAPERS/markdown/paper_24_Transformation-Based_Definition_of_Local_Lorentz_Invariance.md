# Paper 23: Additive Decomposition of Light-Travel Time

## Bibliografische Daten
- **Titel:** Additive Decomposition of the Observed Light-Travel Time
- **Autoren:** Carmen N. Wrede, Lino P. Casu, Bingsi

---

## Zusammenfassung

Dieses Paper zeigt, wie die beobachtete Lichtlaufzeit in geometrische und Segment-Komponenten zerlegt werden kann.

---

## Kernaussagen

1. **Laufzeit = Geometrie + Segmentierung**
2. **Additive Zerlegung** ermöglicht Separation
3. **Shapiro-Delay** als Segment-Effekt

---

## Formeln

### Formel 1: Totale Laufzeit

```
t_total = t_geo + t_seg
```

**Wobei:**
- t_geo = geometrische (flache) Laufzeit
- t_seg = Segment-Korrektur

---

### Formel 2: Geometrische Komponente

```
t_geo = (1/c) âˆ« dr = Î”r/c
```

Standard-Lichtlaufzeit.

---

### Formel 3: Segment-Komponente

```
t_seg = (1/c) âˆ« Îž(r) dr
```

Zusätzliche Zeit durch Segmentierung.

---

### Formel 4: Totale Form

```
t_total = (1/c) âˆ« (1 + Îž(r)) dr = (1/c) âˆ« s(r) dr
```

Mit s(r) = 1 + Îž(r) wie in Maxwell Gauge Paper.

---

### Formel 5: Shapiro-Delay

```
Î”t_Shapiro = t_seg = (1/c) âˆ« Îž(r) dr
```

**Bedeutung:** Shapiro-Delay ist die Segment-Komponente!

---

## Anwendungen

| System | t_geo | t_seg | t_total |
|--------|-------|-------|---------|
| GPS | ~0.067s | ~45 μs/Tag | ~0.067s |
| Sonne (Rand) | ~500s | ~5 μs | ~500s |
| BH (10 r_s) | abhängig | dominiert | >> t_geo |

---

*Erstellt: 2025-12-28*
