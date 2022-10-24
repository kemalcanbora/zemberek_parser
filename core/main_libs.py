import re, ssl
from collections import Counter
import snowballstemmer
from nltk import download
from nltk.corpus import stopwords
import jpype
import os
from core.settings import *


## KULLANIMI ##
###############
# 1) Örnek corpusun cümlelerini parcalara ayırır fonksiyonu ile parçalanır kelime-kelime haline getirilir
#    ve gereksiz kelimeler atılır
# 2) Parçalara ayrılmış olan haber cümlenin öğelerine ayrılır
# 3) Cümlenin öğelerine ayrılmış olan kelimelerin kökleri bulunur bir listeye konulur


class zemberek_api:
    def __init__(self,
                 libjvmpath=libjvmpath,
                 zemberekJarpath=zemberekJarpath):

        if libjvmpath is None:
            libjvmpath = jpype.getDefaultJVMPath()

        self.libjvmpath = libjvmpath

        if zemberekJarpath is None:
            zemberekJarpath = os.path.join(os.path.dirname(__file__), 'zemberek-tum-2.0.jar')
            assert os.path.exists(zemberekJarpath)
        self.zemberekJarpath = zemberekJarpath

    def zemberek(self):
        try:
            if not jpype.isJVMStarted():
                jpype.startJVM(jvmpath=self.libjvmpath, classpath=[self.zemberekJarpath])
            TurkiyeTurkcesi = jpype.JClass("net.zemberek.tr.yapi.TurkiyeTurkcesi")
            turkiye_turkcesi = TurkiyeTurkcesi()

            Zemberek = jpype.JClass("net.zemberek.erisim.Zemberek")
            zemberek_r = Zemberek(turkiye_turkcesi)
            return zemberek_r
        except:
            print("libjvm veya zemberek.jar dosyalarının pathleri yanlış yerde! ")


class ZemberekTool:

    def __init__(self,
                 libjvmpath=libjvmpath,
                 zemberekJarpath=zemberekJarpath):
        super(ZemberekTool, self).__init__()
        self.zemberekapi = zemberek_api(libjvmpath, zemberekJarpath).zemberek()

    def separator(self, text):
        sperator_r = re.sub(r'[^\w\s]', ' ', text).lower()
        sperator_r = ' '.join(sperator_r.split())

        return sperator_r

    def frekans(self, list_x):
        counts = Counter(list_x)

        return counts

    def cumleyi_parcalara_ayir(self, corpus):
        body = self.separator(str(corpus))
        corpus_with_split = self.frekans(body.split())
        stopwords_list = stopwords.words('turkish')
        filtered_words = [word for word in corpus_with_split if word not in stopwords_list]
        return filtered_words

    def ogelere_ayir(self, kelime):
        ## bu  kısım tekil kelime
        result = self.zemberekapi.kelimeCozumle(kelime)

        if len(result) < 1:
            return None

        result = str(result[0])  # java yanıtını str'e dönüştürdüm
        result = result.replace("}", "").replace("  ", " ")

        icerik = re.search('Icerik: (.*) Kok: ', result).group(1)
        kok = re.search('Kok: (.*) tip:', result).group(1)
        tip = re.search(' tip:(.*) Ekler:', result).group(1)
        ekler = re.search(' Ekler:(.*)', result).group(1)

        return dict(icerik=icerik,
                    kok=kok,
                    tip=tip,
                    ekler=ekler)

    def metinde_gecen_kokleri_bul(self, corpus):
        kelimeler = self.cumleyi_parcalara_ayir(corpus)
        metin_kokler_lst = []
        snow = snowballstemmer.stemmer('turkish')
        for i, item in enumerate(kelimeler):
            ## None degerlerin kok,içerik vs olmadıgı için NoneType hatası veriyor bu yüzden try-exp
            ## eger tip bulmak istersen tip;ekler bulmak istersen ekler yaz ogelere_ayir fonksiyonunun dict kısmına bakabilirsin
            try:
                sonuc = self.ogelere_ayir(kelimeler[i])["Kok"]
                metin_kokler_lst.append(sonuc)
            except:
                snow_result = snow.stemWord(kelimeler[i])
                metin_kokler_lst.append(snow_result)

        return metin_kokler_lst

    def kelime_onerici(self, kelime):

        return self.zemberekapi.oner(kelime)

    def kelime_hecele(self, kelime):
        try:
            return self.zemberekapi.hecele(kelime)
        except:
            print(" '\033[1m'  << Kelime_hecele fonksiyonu >> Birden fazla kelime girdiniz")


class nltk_download:
    def __init__(self):
        try:
            _create_unverified_https_context = ssl._create_unverified_context
        except AttributeError:
            pass
        else:
            ssl._create_default_https_context = _create_unverified_https_context
        download()
