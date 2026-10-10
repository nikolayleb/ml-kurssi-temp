# Viikko 41: Dimensiovähennys (PCA ja t-SNE)

Tällä viikolla kokeilin dimensiovähennystä kahdella eri menetelmällä: PCA:lla ja t-SNE:llä. Testasin niitä ensin Drawdata-työkalulla (2D-pisteet) ja sen jälkeen MNIST-numerodatalla.

## 1. Menetelmien perusidea

- **PCA:** Lineaarinen menetelmä. Se etsii suunnat, joissa data vaihtelee eniten, ja kääntää akselit niiden mukaan. Se säilyttää datan yleisen muodon, mutta ei toimi hyvin, jos data on mutkikasta tai käyrää.
- **t-SNE:** Epälineaarinen menetelmä. Se katsoo vain sitä, mitkä pisteet ovat lähellä toisiaan (naapureita). Se löytää erilliset ryhmät ja klusterit tosi hyvin.

## 2. Kokeet Drawdata-pisteillä

Piirsin eri muotoja ja katsoin, miten menetelmät muuttavat niitä:

### Risti (X-muoto)
PCA keskittää pisteet ja kääntää ne, mutta ristin keskellä eri luokat menevät päällekkäin. PCA on suora menetelmä, joten se ei osaa erottaa leikkaavia viivoja.

![X PCA](../images/w41_x_pca.png)

### Rinnakkaiset viivat (II-muoto)
PCA kääntää viivat ja säilyttää niiden suoruuden ja välin. t-SNE taas tekee kummastakin viivasta oman tiiviin nauhan. Molemmat erottavat luokat hyvin.

![II PCA](../images/w41_parallel_lines_pca.png)

![II t-SNE](../images/w41_parallel_lines_tsne.png)

### S-muoto (mutkitteleva viiva)
Tässä näkyy iso ero: PCA pitää S-muodon ennallaan, mutta t-SNE vetää mutkittelevan nauhan suoraksi, koska se keskittyy vain vierekkäisiin pisteisiin.

![S t-SNE](../images/w41_s_shape_tsne.png)

### Windows-logo (4 ryhmää)
Kun pisteet ovat selkeästi omissa kulmissaan, molemmat menetelmät toimivat hyvin. t-SNE kerää ryhmät vielä tiiviimmiksi palloiksi.

![Windows t-SNE](../images/w41_windows_clusters.png)

## 3. MNIST-numerot (kuvadatan tiivistäminen)

MNIST-kuvissa on 64 pikseliä (8x8), ja ne tiivistettiin kahteen ulottuvuuteen:
- **PCA:** Numerot ryhmittyvät vähän, mutta monet numerot menevät sekaisin, koska 2 ulottuvuutta lineaarisesti ei riitä kuville.
- **t-SNE:** Jakaa numerot (0–9) tosi selkeiksi omiksi saarekkeiksi ilman, että malli tiesi numeroita etukäteen.

![MNIST PCA](../images/w41_mnist_pca.png)

![MNIST t-SNE](../images/w41_mnist_tsne.png)