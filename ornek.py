from zemberek_python import main_libs as ml

zemberek_api = ml.zemberek_api(libjvmpath="/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/amd64/server/libjvm.so",
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

# nltk files download ##
z = ml.nltk_download()
