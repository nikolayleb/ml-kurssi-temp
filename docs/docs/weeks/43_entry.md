# Viikko 43: Lineaarinen regressio ja normaaliyhtälö

## 1. Johdanto ja viikon tavoitteet

Tällä viikolla tutustuin lineaariseen regressioon. Toisin kuin aiemmin luokittelussa tai klusteroinnissa, regressiossa tavoitteena on ennustaa jatkuvaa numeroarvoa.

Viikon tärkeimmät asiat olivat:
- Ymmärtää suoran sovittaminen datapisteisiin yhtälöllä y = mx + b.
- Katsoa jäännöstermejä (residuaalit) sekä pienimmän neliösumman kriteeriä (SSE, Ordinary Least Squares).
- Kokeilla normaaliyhtälöä w = inv(X^T * X) * X^T * y, jolla parhaat kertoimet saadaan suoraan matriisilaskulla ilman iteratiivista optimointia.
- Pohtia normaaliyhtälön ongelmia: multikollineaarisuus vaikeuttaa matriisin kääntämistä ja iso piirremäärä tekee laskennasta hidasta.
- Testata ali- ja ylisovittumista muuttamalla polynomin astelukua.

---

## 2. Tehtävä 600: Pienimmän neliösumman menetelmä (Marimo)

Tein tehtävän interaktiivisessa Marimo-muistiossa (`600_least_squares_problem.py`). Tein aluksi `drawdata`-työkalulla aaltomaisen pisteparven, jossa oli selkeää epälineaarisuutta. Sen jälkeen sovitin siihen erilaisia malleja.

### 2.1 Manuaalinen suoran sovittaminen

Ensimmäisessä vaiheessa yritin sovittaa suoraa käsin. Säädin kulmakerrointa m ja vakiotermiä b.

![Suoran manuaalinen sovittaminen](../images/least_squares_manual_fit.png)

Kuten kuvaajasta näkyy, valitsemillani arvoilla (m = 0.50, b = 0.10) neliösumma (SSE) oli **20.89**. Suora viiva ei mitenkään sovi aaltomaiseen dataan. Residuaalit eli punaiset katkoviivat jäävät vielä todella pitkiksi.

### 2.2 Analyyttinen ratkaisu ja asteen 1 regressio

Seuraavaksi laskin parhaan suoran suoraan normaaliyhtälöllä ja kokeilin myös Scikit-Learnin valmista `LinearRegression`-mallia.

![Analyyttinen ratkaisu asteen 1 polynomilla](../images/least_squares_analytical_deg1.png)

Molemmat tavat antoivat täysin saman tuloksen:
- **Normal Equation SSE:** 11.37
- **LinearRegression SSE:** 11.37
- **Polynomial (degree=1) SSE:** 11.37

Vaikka analyyttinen kaava löytää parhaan mahdollisen suoran ja virhe puolittuu, malli kärsii selvästi **alisovittumisesta (underfitting)**. Suora viiva on liian yksinkertainen tällaiselle kaarevalle datalle.

### 2.3 Polynomiregression sovittaminen (degree = 4)

Korjasin alisovittumisen lisäämällä malliin joustavuutta. Kasvatin polynomin astelukua neljään asti (`degree=4`).

![Polynomiregressio asteella 4](../images/least_squares_polynomial_fit.png)

Kun asteen arvoksi laitettiin 4, mallin virhe pieneni huomattavasti:
- **Polynomial (degree=4) SSE:** **2.20**

Neljännen asteen polynomi seuraa datan aaltomaista muotoa tosi siististi. Se ei myöskään tartu liikaa satunnaiseen kohinaan. Jos asteen nostaisi liian korkeaksi (esimerkiksi asteille 8–12), tulisi vastaan **ylisovittuminen (overfitting)**. Silloin käyrä tekisi jyrkkiä mutkia ja yrittäisi osua jokaiseen pisteeseen.

---

## 3. Havainnot ja itsearviointi

- **Analyyttinen vs. iteratiivinen:** Normaaliyhtälö antaa heti tarkan vastauksen pienelle datalle. Huono puoli on kuitenkin matriisin kääntämisen raskaus (aikavaativuus kasvaa jyrkästi piirteiden määrän mukaan) ja se, että liikaa toisistaan riippuvat piirteet estävät matriisin kääntämisen.
- **Residuaalit:** Neliösumma rankaisee isoista heitoista todella paljon enemmän kuin pienistä virheistä. Siksi malli yrittää välttää kaukana olevia pisteitä.
- **Monimutkaisuuden säätö:** Polynomin asteen kasvattaminen laskee aina opetusdatan virhettä. Ilman validointia liian iso aste kuitenkin johtaa ylisovittumiseen ja huonoon ennustekykyyn uudella datalla