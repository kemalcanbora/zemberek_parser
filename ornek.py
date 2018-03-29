from zemberek_python import main_libs as ml


corpus = "merhaba bu bir python zemberek denemesidir,             bu denemeden garip yazılar"
## kelimeyi ögelerine ayır
a = ml.ZemberekTool().ogelere_ayir("bakamadıklarımızdan")
print(a)

## cümleyip gereksiz eklerden bosluklardan ayırır temizler sunar
b = ml.ZemberekTool().cumleyi_parcalara_ayir(corpus)
print(b)

## cümlede geçen kökleri bulur
c = ml.ZemberekTool().metinde_gecen_kokleri_bul(corpus)
print(c)

## kelime_onerici ##
d = ml.ZemberekTool().kelime_onerici("abuzer")
print(d)

## kelime_hecele ##
e = ml.ZemberekTool().kelime_hecele("abdulkadir")
print(e)

## nltk files download ##
# z = ml.nltk_download()
