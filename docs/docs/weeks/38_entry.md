# Viikko 38: Johdatus koneoppimiseen

## 1. Peruskäsitteet ja hierarkia

Tällä viikolla luin materiaalit tekoälyn perusteista. Tärkein juttu on se että AI ja koneoppiminen ei ole sama asia:
* **Tekoäly (AI)** on iso yläkäsite. Se voi olla vain tavallinen koodi ja `if-else` säännöt, esimerkiksi shakkipeli tai A* haku ilman mitään oppimista.
* **Koneoppiminen (ML)** on osa tekoälyä. Tässä kone oppii suoraan datasta ja kokemuksesta (Tom Mitchellin kaava: T, P ja E). Ennen vanhaan Suomessa puhuttiin hahmontunnistuksesta.
* **Syväoppiminen (Deep learning)** on neuroverkkoja. Kurssilla sanottiin selvästi että niitä ei käsitellä nyt, vaan keskitytään 90-luvun klassisiin malleihin.

## 2. Kolme oppimistyyppiä

Koneoppiminen jaetaan kolmeen osaan:
1. **Ohjattu oppiminen (Supervised):** Meillä on $X$ (piirteet) ja tiedetään oikea vastaus $y$. Se on joko luokittelu (onko kissa vai koira) tai regressio (talon hinta numeroina).
2. **Ohjaamaton oppiminen (Unsupervised):** Ei ole valmiita vastauksia. Etsitään vain ryhmiä datasta, kuten t-paitojen koot S, M, L klusteroinnilla tai etsitään poikkeamia palvelimen lämpötilasta.
3. **Vahvistusoppiminen (Reinforcement):** Ei ole valmista datasettiä. Botti kokeilee itse ympäristössä ja saa pisteitä tai miinusta, kuten Pac-Man pelissä tai autopelissä.

Ero algoritmin ja mallin välillä: algoritmi on vain kaava tai koodikirjaston työkalu, mutta malli on se valmis lopputulos kun algoritmi on ajettu datan läpi ja se oppi parametrit.

## 3. Data ja piirteet (Feature extraction)

Tietokone ei ymmärrä kuvia tai tekstiä sellaisenaan. Neuroverkot voi ottaa suoraan pikseleitä, mutta klassisessa ML:ssä ihmisen pitää itse tehdä piirteet (features). Esimerkiksi lomakuvista lasketaan vihreän värin määrä tai reunat, ja annetaan mallille vain lista numeroita.

Opiskeltiin myös neljä mittaustasoa:
* Nominaalinen: nimet ilman järjestystä (esim. automerkit). Pitää muuttaa One-hot koodauksella numeroiksi.
* Ordinaalinen: selkeä järjestys mutta ei välimatkaa (koot S, M, L tai työpaikan roolit).
* Intervalli: kuten Celsius-asteet, nolla ei tarkoita ettei lämpöä ole.
* Suhdeasteikko: normaali numero missä nolla on oikeasti nolla (pituus, paino, eurot).

## 4. Työnkulku ja kurssin esimerkkikoodit

Projektin vaiheet menee yleensä näin: ongelman määrittely -> datan haku -> tutkiminen (EDA) -> esikäsittely -> mallien kokeilu -> säätö -> esittely -> käyttöönotto. Datan laatu on tärkeämpää kuin hieno malli. Myöhemmin malli voi myös vanheta (model drift), joten se pitää opettaa uudestaan.

Pohjustin kehitysympäristön ja kloonasin kurssin notebookit omaan kansioon. Katsoin läpi tiedostoja `130_data_handling_basics.py` ja `131_vector_from_scratch.py`. Huomasin miten puhdas Python-luokka ja for-loopit ovat hitaita vektorilaskennassa, ja miksi NumPy tekee samat asiat paljon nopeammin vektoroidusti. Polars taas vaikuttaa kätevältä ja nopeammalta tavalta käsitellä taulukoita kuin vanha Pandas.

Työnkulku-luvussa oli myös hyvä esimerkki siitä miten mallia tuunataan (hyperparameter tuning) ja miksi ristiinvalidointia (cross-validation) tarvitaan:

# Esimerkki kurssimateriaalista: parametrien haarukointi ja cross-validation
    alpha_grid = [0.1, 0.5, 1.0, 1.5, 2.0]

    for alpha in alpha_grid:
        clf = linear_model.Lasso(alpha=alpha)
        scores = cross_val_score(clf, X_train, y_train, cv=5)
        print(f"Alpha: {alpha}, Scores: {scores}")

Ideana on testata eri alpha-arvot viidessä osassa (cv=5), jotta malli ei opi testidataa ulkoa vaan osaa ennustaa uutta dataa.

## 5. Oma pohdinta

Viikon tärkein asia oli tajuta että koneoppiminen ei ole taikuutta vaan numeroiden optimointia. Jos data on huonoa tai luokkia on liian vähän, malli ei toimi (kuten materiaalissa ollut lotto-esimerkki `return False`). Oli hyvä huomata että klassisissa malleissa pitää itse miettiä piirteet eikä vain laittaa raakadataa sisään. Työkalut on nyt asennettu ja tästä on hyvä jatkaa eteenpäin.