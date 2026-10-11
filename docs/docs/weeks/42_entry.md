# Viikko 42

## Syklinen enkoodaus (Cyclical Encoding)

Tällä viikolla perehdyin syklisten piirteiden käsittelyyn koneoppimisessa. Esimerkiksi kellonaika, viikonpäivä ja kuukausi toistuvat syklissä.

### Ongelma ja ratkaisu

Tavallisessa numeerisessa muodossa kellonajat 23:00 ja 01:00 ovat kaukana toisistaan ($|23 - 1| = 22$). Oikeasti eroa on kuitenkin vain kaksi tuntia. Tämä vääristää etäisyyteen perustuvia malleja, kuten k-Means-klusterointia.

Ongelma korjataan siirtämällä aika yksikköympyrälle sin- ja cos-funktioilla:
- $x_{sin} = \sin(2\pi \cdot x / x_{max})$
- $x_{cos} = \cos(2\pi \cdot x / x_{max})$

Tällä tavalla 23:00 ja 00:00 pysyvät lähellä toisiaan myös matemaattisesti.

![Kellon syklinen enkoodaus](../images/cyclical_clock.png)

### Havainnot

- Testasin koodia Marimo-muistiossa Polars- ja NumPy-kirjastoilla 24 tunnille.
- Laajensin koodin myös minuuttitasolle (klo 04:42). Kun syklin pituus on $24 \times 60 = 1440$ minuuttia, aika 04:42 (282 min) saa ympyrällä arvot $\sin \approx 0{,}94$ ja $\cos \approx 0{,}33$.