# 39: Tekstin enkoodaus ja Naive Bayes

Tällä viikolla tutustuin kahteen aiheeseen: miten teksti muutetaan numeroiksi (TF-IDF) ja miten Bayesin kaava toimii käytännössä, kun aineistossa on useita ehtoja.
---
## 1. Tekstin muuttaminen numeroiksi ja TF-IDF
Tietokone ei ymmärrä sanoja suoraan. Siksi teksti pitää muuttaa numeroiksi. Jos lasketaan vain sanojen määrä (TF), tavalliset sanat saavat liikaa painoa. Tämän takia käytetään IDF-arvoa. Se pienentää sellaisten sanojen painoarvoa, jotka toistuvat melkein jokaisessa tekstissä.

Tehtävässä lisäsin sanan `kurssi` kaikkiin 10 dokumenttiin ($DF = 10, N = 10$). Kaava laskee sen näin:

$$\log(10 / 10) = \log(1) = 0.0$$

Koska tulos on 0.0, sanan paino nollautui kokonaan. Tämä näyttää käytännössä sen, että jos sana löytyy joka paikasta, se ei auta mallia erottelemaan tekstejä toisistaan.

![TF-IDF kurssi 0](../images/tfidf_kurssi.png)
---
## 2. Tilastot ja Bayes: Suora haku vs. Naive Bayes

Käytin harjoituksessa Tilastokeskuksen dataa. Tavoitteena oli laskea todennäköisyys sille, että henkilö on ylempi toimihenkilö (`sose == 3`).

### Suora laskenta (Direct Estimate)
Yritin ensin suodattaa dataa suoraan näillä ehdoilla:
* tulot yli 70 000 €
* asuinpaikka Pohjois-Suomi
* nainen
* opiskelija (`sose == 6`)
* kieli suomi (`kieli == "fi"`)

Tulokseksi tuli 0 riviä (*Oh no! No lines passed the filter*). Aineisto oli liian pieni näin tarkalle yhdistelmälle. Siksi suora suodatus ei toiminut ollenkaan.

![Suora haku epäonnistuu](../images/direct_estimate_failed.png)

### Naive Bayes
Naive Bayes ratkaisee tämän ongelman. Se laskee jokaisen ehdon todennäköisyyden erikseen ja kertoo ne yhteen. Silloin datasta ei tarvitse löytyä valmista riviä, jossa kaikki ehdot toteutuvat samalla kertaa.

Kun lisäsin uudet ehdot koodiin, laskenta meni läpi ilman virheitä.

![Naive Bayes tulos](../images/bayes_result.png)

Lopullinen todennäköisyys oli **0.00**. Tulos on järkevä, koska opiskelija harvoin tienaa yli 70 000 euroa ja toimii samaan aikaan ylempänä toimihenkilönä. Pääasia kuitenkin oli, että malli pystyi laskemaan todennäköisyyden ilman nollalla jakamista.