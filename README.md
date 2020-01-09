# Zemberek Parser 
Zemberek NLP kütüphanesini Python 3 ile kullanabilmenizi sağlar.

## Kullanım
`libjvmpath` argümanı için kendi yolunuzu yazın. `libjvm.so` dosyasının Windows muadili `jvm.dll`'dir. Bu argümana bir değer verilmez ise `JAVA_HOME` veya `JRE_HOME` ortam değişkenlerine göre otomatik olarak bulunmaya çalışılacaktır. Bu repo ile gelen `zemberek-tum-2.0.jar` dosyasını farklı bir klasöre taşıdıysanız bu yolu da `zemberekJarpath` argümanına atamalısınız.
`stopwords.words('turkish')` komutu ile Türkçe stopwords kullanmak istiyorsanız, `~/nltk_data/corpora/stopwords/turkish` dosyasının var olduğuna emin olunuz.

```python
from zemberek_python import main_libs as ml
zemberek_api = ml.zemberek_api(libjvmpath="/usr/lib/jvm/java-8-oracle/jre/lib/amd64/server/libjvm.so",
                            zemberekJarpath="./zemberek_python/zemberek-tum-2.0.jar").zemberek()

corpus = "merhaba bu bir python zemberek denemesidir,             bu denemeden garip yazılar"
## kelimeyi ögelerine ayır
a = ml.ZemberekTool(zemberek_api).ogelere_ayir("bakamadıklarımızdan")
print(a)

## cümleyip gereksiz eklerden bosluklardan ayırır temizler sunar
b = ml.ZemberekTool(zemberek_api).cumleyi_parcalara_ayir(corpus)
print(b)

## cümlede geçen kökleri bulur
c = ml.ZemberekTool(zemberek_api).metinde_gecen_kokleri_bul(corpus)
print(c)

## kelime_onerici ##
d = ml.ZemberekTool(zemberek_api).kelime_onerici("abuzer")
print(d)

## kelime_hecele ##
e = ml.ZemberekTool(zemberek_api).kelime_hecele("abdulkadir")
print(e)

## nltk files download ##
z = ml.nltk_download()
```

