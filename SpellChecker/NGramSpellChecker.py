from Corpus.Sentence import Sentence
from Dictionary.Word import Word
from MorphologicalAnalysis.FsmMorphologicalAnalyzer import FsmMorphologicalAnalyzer
from NGram.NGram import NGram
from SpellChecker.SimpleSpellChecker import SimpleSpellChecker


class NGramSpellChecker(SimpleSpellChecker):

    __nGram: NGram
    __rootNgram: bool
    __threshold: float

    def __init__(self, fsm: FsmMorphologicalAnalyzer, nGram: NGram, rootNGram: bool):
        """
        A constructor of NGramSpellChecker class which takes a FsmMorphologicalAnalyzer and an NGram as inputs. Then,
        calls its super class SimpleSpellChecker with given FsmMorphologicalAnalyzer and assigns given NGram to the
        nGram variable.

        PARAMETERS
        ----------
        fsm : FsmMorphologicalAnalyzer
            FsmMorphologicalAnalyzer type input.
        nGram : NGram
            NGram type input.
        """
        super().__init__(fsm)
        self.__nGram = nGram
        self.__rootNgram = rootNGram
        self.__threshold = 0.0

    def checkAnalysisAndSetRoot(self, sentence: Sentence, index: int) -> Word:
        """
        Checks the morphological analysis of the given word in the given index. If there is no misspelling, it returns
        the longest root word of the possible analyses.
        @param sentence Sentence to be analyzed.
        @param index Index of the word
        @return If the word is misspelled, null; otherwise the longest root word of the possible analyses.
        """
        if index < sentence.wordCount():
            fsmParses = self.fsm.morphologicalAnalysis(sentence.getWord(index).getName())
            if fsmParses.size() != 0:
                if self.__rootNgram:
                    return fsmParses.getParseWithLongestRootWord().getWord()
                else:
                    return sentence.getWord(index)
        return None

    def setThreshold(self, threshold: float):
        self.__threshold = threshold

    def spellCheck(self, sentence: Sentence) -> Sentence:
        """
        The spellCheck method takes a Sentence as an input and loops i times where i ranges from 0 to size of words in
        given sentence. Then, it calls morphologicalAnalysis method with each word and assigns it to the FsmParseList,
        if the size of FsmParseList is equal to the 0, it adds current word to the candidateList and assigns it to the
        candidates list.

        Later on, it loops through candidates list and calls morphologicalAnalysis method with each word and assigns it
        to the FsmParseList. Then, it gets the root from FsmParseList. For the first time, it defines a previousRoot by
        calling getProbability method with root, and for the following times it calls getProbability method with
        previousRoot and root. Then, it finds out the best probability and the corresponding candidate as best candidate
        and adds it to the result Sentence.

        If the size of FsmParseList is not equal to 0, it directly adds the current word to the result Sentence and
        finds the previousRoot directly from the FsmParseList.

        PARAMETERS
        ----------
        sentence : Sentence
            Sentence type input.

        RETURNS
        -------
        Sentence
            Sentence result.
        """
        previousRoot = None
        result = Sentence()
        root = self.checkAnalysisAndSetRoot(sentence, 0)
        nextRoot = self.checkAnalysisAndSetRoot(sentence, 1)
        for i in range(sentence.wordCount()):
            word = sentence.getWord(i)
            if root is None:
                candidates = self.candidateList(word)
                bestCandidate = word.getName()
                bestRoot = word
                bestProbability = self.__threshold
                for candidate in candidates:
                    fsmParses = self.fsm.morphologicalAnalysis(candidate)
                    if self.__rootNgram:
                        root = fsmParses.getParseWithLongestRootWord().getWord()
                    else:
                        root = Word(candidate)
                    if previousRoot is not None:
                        previousProbability = self.__nGram.getProbability(previousRoot.getName(), root.getName())
                    else:
                        previousProbability = 0.0
                    if nextRoot is not None:
                        nextProbability = self.__nGram.getProbability(root.getName(), nextRoot.getName())
                    else:
                        nextProbability = 0.0
                    if max(previousProbability, nextProbability) > bestProbability:
                        bestCandidate = candidate
                        bestRoot = root
                        bestProbability = max(previousProbability, nextProbability)
                root = bestRoot
                result.addWord(Word(bestCandidate))
            else:
                result.addWord(word)
            previousRoot = root
            root = nextRoot
            nextRoot = self.checkAnalysisAndSetRoot(sentence, i + 2)
        return result
