from zemcore.zemberek.parser import Run, Tool

text = "gezegnde bi vibüs var"
result = Run(text, Tool.SENTENCE_CORRECTOR)
print(result)
