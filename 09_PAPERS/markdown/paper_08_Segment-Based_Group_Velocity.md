# Paper 07: Kinematische SchlieÃŸung â€“ Escape vs. Fall

## Bibliografische Daten
- **Titel:** Kinematische SchlieÃŸung in segmentierter Raumzeit: escape vs. fall
- **Autoren:** Carmen Wrede, Lino Casu
- **Thema:** Formale Herleitung der Dualität

---

## Zusammenfassung

Dieses Paper zeigt formal, wie die duale Beziehung v_esc · v_fall = c² in der segmentierten Raumzeit hergestellt wird. Die SchlieÃŸung entsteht durch Gleichsetzung der lokalen Lorentzfaktoren.

---

## Notation

| Symbol | Bedeutung |
|--------|-----------|
| r_s | Schwarzschild-Radius = 2GM/c² |
| U | GM/(rc²) |
| v_esc | âˆš(2GM/r) = câˆš(r_s/r) |
| γ_GR | (1 - r_s/r)^(-1/2) |
| Ï† | Golden Ratio |

---

## Formeln

### Formel 1: GR-konjugierter Fallwert

```
γ_GR(r) = (1 - r_s/r)^(-1/2) = (1 - (v_fall^GR/c)²)^(-1/2)
```

**Lösung für v_fall:**
```
(v_fall^GR/c)² = r_s/r
v_fall^GR(r) = câˆš(r_s/r)
```

---

### Formel 2: Produkt (Gleichung 2.1)

```
v_esc(r) · v_fall^GR(r) = câˆš(r_s/r) · câˆš(r_s/r) = c²(r_s/r)
```

**Hinweis:** Dies ist noch NICHT die SchlieÃŸung!

---

### Formel 3: Segmentierte Normierung

```
v_fall(r) := (r/r_s) · v_fall^GR(r) = (r/r_s) · câˆš(r_s/r) = câˆš(r/r_s)
```

**Bedeutung:** Skalierter Parameter für produkt-invariante Dualität.

---

### Formel 4: Kinematische SchlieÃŸung (Gleichung 2.3)

```
v_esc(r) · v_fall(r) = câˆš(r_s/r) · câˆš(r/r_s) = c²
```

**KONSTANT für alle r!**

---

### Formel 5: Ï†-Gitter-Variable

```
n*(R) = ln R / ln Ï†
```

**Segmentanzahl:**
```
N = round(n*)
```

**Residual:**
```
ε = n* - N
```

---

### Formel 6: Euler-Hülle

```
R â‰ˆ exp(Î”U)  mit Î”U â‰ˆ N ln Ï†
```

Reproduziert GR; fällt auf Ï†-Gitter wenn N âˆˆ â„¤.

---

### Formel 7: Kopplungspunkt

```
r_Ï† â‰ˆ (Ï†/2) r_s · [1 + Î²·Î”(M)]
```

**Komponenten:**
- Ï†/2 â‰ˆ 0.809
- β = kleine Massenkopplung
- Î”(M) = langsamer Massen-Proxy

---

### Formel 8: β-Term (nicht PPN!)

```
r_Ï†(M; Î²) = r_Ï†[1 + Î²·Î”(M)],  |Î²| << 1
```

**Bedeutung:** Sanfte Verschiebung der Skalenlage.

---

## Physikalisches Bild

1. **AuÃŸen:** GR-Hülle, kontinuierlich, PPN identisch zu GR
2. **Grenzen:** Diskrete Ï†-Schritte in Ratios R
3. **Innen:** Stückweise konstante Skalen, C²-Blend um r_Ï†
4. **Messung:** Nur Ratios und Gitterstruktur

---

## Interpretation von v_fall

v_fall nach Formel 3 ist:
- **KEIN** physikalischer 3-Geschwindigkeitswert
- Ein **Dual-Parameter** des SSZ-Formalismus
- Die **reziproke Skalenkopplung**
- Die **operative Brücke** zwischen Energiebilanz und Segmentierung

---

## Gültigkeitsbereich

| Gleichung | Gültigkeit |
|-----------|------------|
| (2.1) v_esc · v_fall^GR = c²(r_s/r) | Allgemein Schwarzschild |
| (2.3) v_esc · v_fall = c² | SSZ-Definition |

---

*Erstellt: 2025-12-28*
