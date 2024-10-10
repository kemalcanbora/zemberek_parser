import xml.etree.ElementTree as ET
import os

class TurkishWordNet:
    def __init__(self, wordnet_file_path="turkish1998_wordnet.xml"):
        file_path = os.path.join(os.path.dirname(__file__), wordnet_file_path)
        self.synsets = self._parse_turkish_wordnet_xml(file_path)
        self.synonym_dict = self._create_synonym_dict()

    def _parse_turkish_wordnet_xml(self, file_path):
        tree = ET.parse(file_path)
        root = tree.getroot()
        synsets = {}

        for synset in root.findall(".//SYNSET"):
            synset_id = synset.find('ID').text
            pos = synset.find('POS').text
            definition = synset.find('DEF').text
            literals = [literal.text for literal in synset.findall('.//LITERAL')]
            example = synset.find('EXAMPLE')
            example_text = example.text if example is not None else None

            synsets[synset_id] = {
                'pos': pos,
                'definition': definition,
                'literals': literals,
                'example': example_text
            }

        return synsets

    def _create_synonym_dict(self):
        synonym_dict = {}

        for synset_info in self.synsets.values():
            literals = synset_info['literals']
            for literal in literals:
                if literal not in synonym_dict:
                    synonym_dict[literal] = set()
                synonym_dict[literal].update(set(literals) - {literal})

        return synonym_dict

    def get_synonyms(self, word):
        return list(self.synonym_dict.get(word, []))

    def get_word_info(self, word):
        synonyms = self.get_synonyms(word)
        word_info = []

        for synset_id, synset_info in self.synsets.items():
            if word in synset_info['literals']:
                word_info.append({
                    'pos': synset_info['pos'],
                    'definition': synset_info['definition'],
                    'synonyms': synonyms,
                    'example': synset_info['example']
                })

        return word_info
