from abc import abstractmethod

from Corpus.Sentence import Sentence


class SpellChecker:

    @abstractmethod
    def spellCheck(self, sentence: Sentence) -> Sentence:
        """
        The spellCheck method which takes a Sentence as an input.

        PARAMETERS
        ----------
        sentence : Sentence
            Sentence type input.

        RETURNS
        -------
        Sentence
            Sentence result.
        """
        pass
