from fonksiyonlar import main_libs as ml

corpus="merhaba bu bir python zemberek denemesidir,             bu denemeden garip yazılar"

## kelimeyi ögelerine ayır
a=ml.ogelere_ayir("bakamadıklarımızdan")
print(a)

## cümleyip gereksiz eklerden bosluklardan ayırır temizler sunar
b=ml.cumleyi_parcalara_ayir(corpus)
print(b)

## cümlede geçen kökleri bulur
c=ml.metinde_gecen_kokleri_bul(corpus)
print(c)

## kelime_onerici ##
d= ml.kelime_onerici("abuzer")
print(d)

## kelime_hecele ##
e=ml.kelime_hecele("abdulkadir")