import os

from zemcore.zemberek.main_libs import nltk_download, ZemberekTool
from zemcore.kefir_.subject import Person
from zemcore.kefir_.predication import personal, inferential
from zemcore.spellChecker.simple_spell_checker import SimpleSpellChecker

from MorphologicalAnalysis.FsmMorphologicalAnalyzer import FsmMorphologicalAnalyzer
from Corpus.Sentence import Sentence

zemberekTool = ZemberekTool()


class Tool:
    KELIMEYI_OGELERINE_AYIR: str = "KELIMEYI_OGELERINE_AYIR"
    CUMLEDE_GECEN_KOKLERI_BUL: str = "CUMLEDE_GECEN_KOKLERI_BUL"
    CUMLEYI_PARCALARA_AYIR: list = "CUMLEYI_PARCALARA_AYIR"
    KELIME_ONERICI: str = "KELIME_ONERICI"
    KELIME_HECELE: str = "KELIME_HECELE"
    NLTK_FILES_DOWNLOAD: str = "NLTK_FILES_DOWNLOAD"
    PERSONIFICATION_COPULA: str = "PERSONIFICATION_COPULA"
    INFERENTIAL_MOOD: str = "INFERENTIAL_MOOD"
    CONVERT_PDF_TO_TXT: str = "CONVERT_PDF_TO_TXT"
    SENTENCE_CORRECTOR: str = "SENTENCE_CORRECTOR"


class Run(Tool):
    def __init__(self, corpus, example, pdf_path=None):
        self.corpus = corpus
        self.example = example
        self.result = None
        self.pdf_path = pdf_path

        if self.example == Tool.KELIMEYI_OGELERINE_AYIR:
            self.result = zemberekTool.ogelere_ayir(corpus)
            if self.result is None:
                self.result = "Cümle yerine kelime girmeniz gerekiyor veya girdiğiniz kelime yanlış"

        if self.example == Tool.CUMLEDE_GECEN_KOKLERI_BUL:
            self.result = zemberekTool.metinde_gecen_kokleri_bul(self.corpus)

        if self.example == Tool.CUMLEYI_PARCALARA_AYIR:
            self.result = zemberekTool.cumleyi_parcalara_ayir(self.corpus)

        if self.example == Tool.KELIME_ONERICI:
            self.result = zemberekTool.kelime_onerici(self.corpus)
            if self.result is None:
                self.result = "Cümle yerine kelime girmeniz gerekiyor"

        if self.example == Tool.KELIME_HECELE:
            self.result = zemberekTool.kelime_hecele(self.corpus)
            if self.result is None:
                self.result = "Cümle yerine kelime girmeniz gerekiyor"

        if self.example == Tool.NLTK_FILES_DOWNLOAD:
            self.result = nltk_download()

        if self.example == Tool.PERSONIFICATION_COPULA:
            self.result = personal(self.corpus, Person.FIRST, is_plural=True)
            if self.result is None:
                self.result = "Cümle yerine kelime girmeniz gerekiyor"

        if self.example == Tool.INFERENTIAL_MOOD:
            self.result = inferential(self.corpus, Person.SECOND, is_plural=False)
            if self.result is None:
                self.result = "Cümle yerine kelime girmeniz gerekiyor"

        if self.example == Tool.SENTENCE_CORRECTOR:
            path = os.path.dirname(os.path.realpath(__file__))
            fsm = FsmMorphologicalAnalyzer(path+"/turkish_dictionary.txt",
                                           path+"/turkish_misspellings.txt",
                                           path+"/turkish_finite_state_machine.xml")

            spellChecker = SimpleSpellChecker(fsm)
            sentence = Sentence(self.corpus)
            self.result = spellChecker.spellCheck(sentence)

    def __str__(self):
        return str(self.result)
