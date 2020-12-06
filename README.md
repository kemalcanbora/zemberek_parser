# Zemberek Parser 
Zemberek NLP kütüphanesini Python 3 ile kullanabilmenizi sağlar.

## Kullanım
Eğer ubuntu ve java-8-openjdk kullanıyorsanız otomatik olarak çalışacaktır diğer durumlarda
setting.py içerisinde `libjvmpath` argümanı için kendi yolunuzu yazın. `libjvm.so` dosyasının Windows muadili `jvm.dll`'dir. Bu argümana bir değer verilmez ise `JAVA_HOME` veya `JRE_HOME` ortam değişkenlerine göre otomatik olarak bulunmaya çalışılacaktır. Bu repo ile gelen `zemberek-tum-2.0.jar` dosyasını farklı bir klasöre taşıdıysanız bu yolu da `zemberekJarpath` argümanına atamalısınız.
`stopwords.words('turkish')` komutu ile Türkçe stopwords kullanmak istiyorsanız, `~/nltk_data/corpora/stopwords/turkish` dosyasının var olduğuna emin olunuz. Ek hatırlatma eğer isterseniz ZemberekTool() içerisine libjvmpath,
zemberekJarpath değişkenleri aracılığı ile path verebilirsiniz.

```
zemberekTool = ZemberekTool(libjvmpath = libpath, 
                            zemberekJarpath = zemberekJaryolu )
```

#### Genel Bakış
```python
from zemberek_python.main_libs import nltk_download, ZemberekTool
from kefir.predication import personal, inferential
from kefir.subject import Person

zemberekTool = ZemberekTool()


corpus = "merhaba bu bir python zemberek denemesidir, bu denemeden garip yazılar"


## kelimeyi ögelerine ayır
a = zemberekTool.ogelere_ayir("bakamadıklarımızdan")
print(a)

## cümleyip gereksiz eklerden bosluklardan ayırır temizler sunar
b = zemberekTool.cumleyi_parcalara_ayir(corpus)
print(b)

## cümlede geçen kökleri bulur
c = zemberekTool.metinde_gecen_kokleri_bul(corpus)
print(c)

## kelime_onerici ##
d = zemberekTool.kelime_onerici("abuzer")
print(d)

## kelime_hecele ##
e = zemberekTool.kelime_hecele("abdulkadir")
print(e)

# nltk files download ##
download_NLTK = nltk_download()

# personification copula
test1 = personal('gezegenli', Person.FIRST, is_plural=True)
print(test1)

# inferential mood (-miş in turkish)
test2 = inferential('öğretmen', Person.SECOND, is_plural=False)
print(test2)
```


##### Yeni yenilik notları
 - <a href="https://github.com/yogurt-cultures/kefir">Kefir</a> eklendi! 
 - Buglar düzeltildi bir tık daha derli toplu oldu
 - PDFleri metine dönüştürme fonksiyonu eklendi
