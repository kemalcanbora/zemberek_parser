# Zemberek Parser 
Turkce icin NLP kutuphanesi.

```python
from zemberek import  TurkishWordNet

turkish_wn = TurkishWordNet()

# Example usage
word = "acayip"
word_info = turkish_wn.get_word_info(word)

if word_info:
    for info in word_info:
        print(f"Word: {word}")
        print(f"Part of Speech: {info['pos']}")
        print(f"Definition: {info['definition']}")
        print(f"Synonyms: {', '.join(info['synonyms'])}")
        if info['example']:
            print(f"Example: {info['example']}")
        print()
else:
    print(f"No information found for the word: {word}")

# output:
# Word: acayip
# Part of Speech: a
# Definition: Sağduyuya, göreneğe, olağana aykırı, yadırganan
# Synonyms: yabansı, çok şey, garip, cins
# Example: Acayip kıyafet
```

 
##### Bug ve Diğer durumlar
 - Kütüphaneyi kullandığınızda karşılaştığınız hataları belirtirseniz (PR, MR açabilirsiniz veya direk <a href="https://www.linkedin.com/in/kemalcan-bora-8b702926/"> bana </a> ulaşabilirsiniz)
 - Tez veya çalışmanızda repoyu kaynak verirseniz başka insanlar da faydalanabilir.

#### CoLab
 - `!apt-get install openjdk-8-jdk-headless -qq > /dev/null`
 - `!pip install git+https://github.com/kemalcanbora/zemberek_parser.git`