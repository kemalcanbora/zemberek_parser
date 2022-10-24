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
MacOS'da otomatik olarak jar dosyasını bulamıyor zemberek_python içerisinde ekli olan dosyanın yolunu verebilirsiniz. Settings.py dosyasını editleyebilirsiniz.


#### Genel Bakış
```python

# Tool'da bulunan bazı fonksiyonlar
    - KELIMEYI_OGELERINE_AYIR
    - CUMLEDE_GECEN_KOKLERI_BUL
    - CUMLEYI_PARCALARA_AYIR
    - KELIME_ONERICI
    - KELIME_HECELE
    - NLTK_FILES_DOWNLOAD
    - PERSONIFICATION_COPULA
    - INFERENTIAL_MOOD
    - CONVERT_PDF_TO_TXT
    - SENTENCE_CORRECTOR
```
#### Örnekler

```python
from zemcore.zemberek.parser import Run, Tool

text = "merhaba"
result = Run(text, Tool.KELIME_HECELE)
print(result)

# output: ['mer', 'ha', 'ba']

```

```python
from zemcore.zemberek.parser import Run, Tool

text = "gezegnde bi vibüs var"
result = Run(text, Tool.SENTENCE_CORRECTOR)
print(result)
# output:  gezende bir virüs var
```


##### Yeni yenilik notları
 - <a href="https://github.com/yogurt-cultures/kefir">Kefir</a> eklendi! 
 - Buglar düzeltildi bir tık daha derli toplu oldu
 - PDFleri metine dönüştürme fonksiyonu eklendi
 - <a href="https://github.com/StarlangSoftware/TurkishSpellChecker-Py"> TurkishSpellChecker-Py </a> eklendi

##### Bug ve Diğer durumlar
 - Kütüphaneyi kullandığınızda karşılaştığınız hataları belirtirseniz (PR, MR açabilirsiniz veya direk <a href="https://www.linkedin.com/in/kemalcan-bora-8b702926/"> bana </a> ulaşabilirsiniz)
 - Tez veya çalışmanızda repoyu kaynak verirseniz başka insanlar da faydalanabilir.

#### CoLab
 - `!apt-get install openjdk-8-jdk-headless -qq > /dev/null`
 - `!pip install git+https://github.com/kemalcanbora/zemberek_parser.git`