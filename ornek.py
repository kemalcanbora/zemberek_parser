import time

from zemberek import (
    TurkishSpellChecker,
    TurkishMorphology,
    TurkishTokenizer,
    TurkishWordNet
)


morphology = TurkishMorphology.create_with_defaults()

sc = TurkishSpellChecker(morphology)


# SPELLING SUGGESTION
li = ["okuyablirim", "tartısıyor", "Ankar'ada", "knlıca", "yapablrim", "kıredi", "geldm", "geliyom", "aldm", "asln"]
start = time.time()
for word in li:
    print(word + " = " + ' '.join(sc.suggest_for_word(word)))


# SENTENCE ANALYSIS AND DISAMBIGUATION
sentence = "Yarın kar yağacak."
analysis = morphology.analyze_sentence(sentence)
after = morphology.disambiguate(sentence, analysis)

print("\nBefore disambiguation")
for e in analysis:
    print(f"Word = {e.inp}")
    for s in e:
        print(s.format_string())

print("\nAfter disambiguation")
for s in after.best_analysis():
    print(s.format_string())

# TOKENIZATION
tokenizer = TurkishTokenizer.DEFAULT

tokens = tokenizer.tokenize("Saat 12:00.")
for token in tokens:
    print('Content = ', token.content)
    print('Type = ', token.type_.name)
    print('Start = ', token.start)
    print('Stop = ', token.end, '\n')



