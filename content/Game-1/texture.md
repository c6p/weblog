Title: Doku
Date: 2014-08-06 21:47
Slug: texture
Lang: tr

UV koordinatlarını oluşturdum ve aşağıdaki dokuyla kapladım. Koordinatlar altıgen şeklinde, ancak kolaya kaçmak için basit bir test resmi kullandım.

![Doku resmi](static/tile.png)

Altıgenleri test amacıyla rastgele kapladım.

<div markdown="span" class="video-container">
<img class="gfyitem" data-id="SnivelingCaringAmericanwigeon"/>
</div>

Aslında pazartesi günü bu kısmı yazmıştım, iki günümü hata ayıklamakla geçirdim. Önce sorunun shaderda olduğunu düşünüp, yeni bir shader yazdım. Ya da bir şekilde koordinatların ekran kartına gönderilmediğinden şüphelenip hatayı Horde3D'de aradım. Ama hep söyledikleri gibi hata büyük olasılıkla sendedir, zira bu kütüphaneler iyi test edilmiştir. En son sorunun gönderdiğim koordinatlarda olduğuna kanaat getirip hesaplama sonrası son değerleri yazdırdım. Düzgündü. Sonunda farkettim ki bu değerleri hesaplattığım fonksiyonun içerisinde kontrol ediyorum, ve koordinat olarak artık geçersiz hale gelen yerel değişkene pointerı gönderiyorum. Önce Ockham'ın Usturası.
