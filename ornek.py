from settings import Run, Tool

text = "gezegnde bi vibüs var"
result = Run(text, Tool.SENTENCE_CORRECTOR)
print(result)
