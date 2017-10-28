from nltk.corpus import stopwords
from zemberek_connection.zem_conn import zemberek
from tools.spector import sperator_fonk
from tools.frekans_bul import frekans

libjvmpath="/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/amd64/server/libjvm.so"
zemberekJarpath="/home/kb/PycharmProjects/zemberek_parser/zemberek_connection/zemberek-tum-2.0.jar"

zemberek_api= zemberek(libjvmpath,zemberekJarpath)



                                ## KULLANIMI ##
                                ###############
# 1) Örnek corpusun cümlelerini parcalara ayırır fonksiyonu ile parçalanır kelime-kelime haline getirilir
#    ve gereksiz kelimeler atılır
# 2) Parçalara ayrılmış olan haber cümlenin öğelerine ayrılır
# 3) Cümlenin öğelerine ayrılmış olan kelimelerin kökleri bulunur bir listeye konulur



def cumleyi_parcalara_ayir(corpus):
    body= sperator_fonk(str(corpus)) ##cümlede gereksiz olan işaretlemeler ve boşluklar silindi
    sonuc = frekans(body.split()) ## haber içersinde kaç tane hangi kelimeden var
    stopwords_list = stopwords.words('turkish')
    filtered_words = [word for word in sonuc if word not in stopwords_list] ## gereksiz bağlaçlar silindi
    return (filtered_words)

def ogelere_ayir(kelime):
    ## bu  kısım tekil kelime
    yanit = zemberek_api.kelimeCozumle(kelime)
    if len(yanit)<1:
        return None
    try:
        x=(str(yanit[0])) #java yanıtını str'e dönüştürdüm
        words = [x.replace('{', '') # elde olan string kısmında saçma sapan kısımları cıkarttım
                     .replace('}', '').replace("Icerik", '')
                     .replace("Kok", '').replace("Ekler", '')
                     .replace(":", '').replace("tip", ' ').replace("  ", ",").replace(" ", "")
                 ]
        words = ','.join(words)
        y = [value for value in words.split(',')]
        dict = ({"Icerik": y[0],# tekrar dict haline getirdim peki neden bu kadar ugras sebebi java class yapısı
                 "Kok":    y[1],
                 "tip":    y[2],
                 "Ekler":  y[3]})
        return (dict)
    except:
        pass

def metinde_gecen_kokleri_bul(corpus):
    haberx=cumleyi_parcalara_ayir(corpus)
    metin_kokler_lst=[]
    for i,item in enumerate(haberx):
        try: ## None degerlerin kok,içerik vs olmadıgı için NoneType hatası veriyor bu yüzden try-exp
            sonuc=(ogelere_ayir(haberx[i])["Kok"])  ## eger tip bulmak istersen tip;ekler bulmak istersen ekler yaz ogelere_ayir fonksiyonunun dict kısmına bakabilirsin
            metin_kokler_lst.append(sonuc)
        except:
            continue
    return metin_kokler_lst

def kelime_onerici(kelime):
    yanit = zemberek_api.oner(kelime)
    ## listeye döndürmek için böyle bir yöntem yaptım şimdilik
    yanit=str(yanit).replace('"',"").replace("(","").replace(")","").replace("'","").split(",")
    return (yanit) # listeye döndürdük

def kelime_hecele(kelime):
    try:
        yanit = zemberek_api.hecele(kelime)
        ## str  ile java string tipini python str tipine dönüştürdüm
        ## listeye döndürmek için böyle bir yöntem yaptım şimdilik

        yanit=(str(yanit).replace('"',"").replace("(","").replace(")","").replace("'","").split(","))

    except   :
        print(" '\033[1m'  << Kelime_hecele fonksiyonu >> Birden fazla kelime girdiniz")


    return yanit

