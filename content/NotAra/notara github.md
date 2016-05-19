Title: NotAra
Date: 2014-08-27 15:50
Slug: notara-github
Lang: tr

PDF annotation'ları gözden geçirme amacı taşıyor. Bu yüzden de araştırma ve organizasyon açısından yetersizler. Ayrıca web sayfaları PDF'den de zengin kaynaklar. Yerimleriyse buna tek başına bir çözüm üretemiyor.  Hali hazırda iki sorunu da çözen birçok uygulama var. Ancak çoğu ya fazla kompleks, ya abonelik bazlı işliyor ve verileri bulutta saklıyor (bu senkronizasyon açısından bir artı olsa da, veri mahremiyeti göz ardı edilse bile bu servislerdeki dosya ya da veritabanı boyutundaki kısıtlamalar engelleyici oluyor), ya gereken özelliklerden yoksunlar ya da PDF ve HTML'den yalnızca birini gösterip üzerine not ekleyebiliyorlar.

[NotAra](https://github.com/c6parmak/NotAra) mümkün olduğunca basit kalarak varolan annotationları içe aktarabildiği gibi, desteklediği döküman tiplerinin hepsi için aynı arayüzle sayfa üzerine not almaya olanak tanıyıp hepsini kategorik olarak düzenlemeyi ve bütün kütüphaneyi aramayı da mümkün kılacak.

![NotAra metin seçimi](static/notara-textselection.png)
: NotAra Metin Seçimi

Henüz sadece PDF sayfaları ekranda gösteriliyor ve metin seçimi yapılabiliyor. Yani çok erken bir safhada. Uygulama arayüz için QtQuick 2 (Qt5) kullanacak, bunun daha sonra annotationları çizerken kolaylık sağlaması umuyorum. Ve belki bir Android portu gündeme gelirse fazla değişiklik yapmadan mümkün kılmasını. Bir miktar Qt4 tecrübem olsa da QtQuick'e yabancıydım. C++ QML iletişimini anlamam epey zamanımı aldı: Poppler'den gelen resimleri ve QML'de seçili alanı C++'da işleyip dikdörtgenleri yeniden QML ile paylaşmak.

Şu anda metin kalitesi (antialiasing ile dahi) öteki Poppler kullanan PDF okuyucuların çok altında. Bu konuyla temel özellikleri yazdıktan sonra ilgileneceğim.

