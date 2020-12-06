from zemberek_python.main_libs import nltk_download, ZemberekTool
from kefir.predication import personal, inferential
from kefir.subject import Person
from tika import pdfconverter

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


# convert pdf to txt
convert = pdfconverter.PDFParser("./example.pdf").parse()
print(convert)
