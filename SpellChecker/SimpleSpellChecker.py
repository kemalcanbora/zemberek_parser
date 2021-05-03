from random import randrange

from Corpus.Sentence import Sentence
from Dictionary.Word import Word
from Language.TurkishLanguage import TurkishLanguage
from MorphologicalAnalysis.FsmMorphologicalAnalyzer import FsmMorphologicalAnalyzer

from SpellChecker.SpellChecker import SpellChecker


class SimpleSpellChecker(SpellChecker):

    fsm: FsmMorphologicalAnalyzer

    def __init__(self, fsm: FsmMorphologicalAnalyzer):
        """
        A constructor of SimpleSpellChecker class which takes a FsmMorphologicalAnalyzer as an input and
        assigns it to the fsm variable.

        PARAMETERS
        ----------
        fsm : FsmMorphologicalAnalyzer
            FsmMorphologicalAnalyzer type input.
        """
        self.fsm = fsm

    def __generateCandidateList(self, word: str) -> list:
        """
        The generateCandidateList method takes a String as an input. Firstly, it creates a String consists of lowercase
        Turkish letters and an list candidates. Then, it loops i times where i ranges from 0 to the length of given
        word. It gets substring from 0 to ith index and concatenates it with substring from i+1 to the last index as a
        new String called deleted. Then, adds this String to the candidates list. Secondly, it loops j times where j
        ranges from 0 to length of lowercase letters String and adds the jth character of this String between substring
        of given word from 0 to ith index and the substring from i+1 to the last index, then adds it to the candidates
        list. Thirdly, it loops j times where j ranges from 0 to length of lowercase letters String and adds the jth
        character of this String between substring of given word from 0 to ith index and the substring from i to the
        last index, then adds it to the candidates list.

        PARAMETERS
        ----------
        word : str
            String input.

        RETURNS
        -------
        list
            List candidates.
        """
        s = TurkishLanguage.LOWERCASE_LETTERS
        candidates = []
        for i in range(len(word)):
            if i < len(word) - 1:
                swapped = word[:i] + word[i + 1] + word[i] + word[i + 2:]
                candidates.append(swapped)
            if word[i] in TurkishLanguage.LETTERS or word[i] in "wqx":
                deleted = word[:i] + word[i + 1:]
                candidates.append(deleted)
                for j in range(len(s)):
                    replaced = word[:i] + s[j] + word[i + 1:]
                    candidates.append(replaced)
                for j in range(len(s)):
                    added = word[:i] + s[j] + word[i:]
                    candidates.append(added)
        return candidates

    def candidateList(self, word: Word) -> list:
        """
        The candidateList method takes a Word as an input and creates a candidates list by calling generateCandidateList
        method with given word. Then, it loop i times where i ranges from 0 to size of candidates list and creates a
        FsmParseList by calling morphologicalAnalysis with each item of candidates list. If the size of FsmParseList is
        0, it then removes the ith item.

        PARAMETERS
        ----------
        word : Word
            Word input.

        RETURNS
        -------
        list
            candidates list.
        """
        candidates = self.__generateCandidateList(word.getName())
        i = 0
        while i < len(candidates):
            fsmParseList = self.fsm.morphologicalAnalysis(candidates[i])
            if fsmParseList.size() == 0:
                newCandidate = self.fsm.getDictionary().getCorrectForm(candidates[i])
                if newCandidate != "" and self.fsm.morphologicalAnalysis(newCandidate).size() > 0:
                    candidates[i] = newCandidate
                else:
                    candidates.pop(i)
                    i = i - 1
            i = i + 1
        return candidates

    def spellCheck(self, sentence: Sentence) -> Sentence:
        """
        The spellCheck method takes a Sentence as an input and loops i times where i ranges from 0 to size of words in
        given sentence. Then, it calls morphologicalAnalysis method with each word and assigns it to the FsmParseList,
        if the size of FsmParseList is equal to the 0, it adds current word to the candidateList and assigns it to the
        candidates list. If the size of candidates greater than 0, it generates a random number and selects an item from
        candidates list with this random number and assign it as newWord. If the size of candidates is not greater than
        0, it directly assigns the current word as newWord. At the end, it adds the newWord to the result Sentence.

        PARAMETERS
        ----------
        sentence : Sentence
            Sentence type input.

        RETURNS
        -------
        Sentence
            Sentence result.
        """
        result = Sentence()
        for i in range(sentence.wordCount()):
            word = sentence.getWord(i)
            fsmParseList = self.fsm.morphologicalAnalysis(word.getName())
            if fsmParseList.size() == 0:
                candidates = self.candidateList(word)
                if len(candidates) > 0:
                    randomCandidate = randrange(len(candidates))
                    newWord = Word(candidates[randomCandidate])
                else:
                    newWord = word
            else:
                newWord = word
            result.addWord(newWord)
        return result
