from natasha import (
    Segmenter,
    MorphVocab,
    NewsEmbedding,
    NewsMorphTagger,
    NewsNERTagger,
    Doc,
)
from source.skill import Skill
from source.utils import get_data_path
import os
import json
from fuzzysearch import find_near_matches


class EntityParser(Skill):
    def __init__(self):
        self.segmenter = Segmenter()
        self.morph_vocab = MorphVocab()
        emb = NewsEmbedding()
        self.morph_tagger = NewsMorphTagger(emb)
        self.ner_tagger = NewsNERTagger(emb)
        self.language_dict = dict()
        self.load_data()

    def load_data(self) -> None:
        with open(
            os.path.join(get_data_path(), "language.json"), "r", encoding="utf-8"
        ) as f:
            self.language_dict = json.load(f)

    def get_answer(self, phrase, context=None) -> str:
        phrase = phrase.title()
        self.doc = Doc(phrase)
        self.doc.segment(self.segmenter)
        self.doc.tag_morph(self.morph_tagger)
        self.doc.tag_ner(self.ner_tagger)
        for span in self.doc.spans:
            span.normalize(self.morph_vocab)
        data = {}
        data["LOC"] = []
        for span in self.doc.spans:
            if span.type == "LOC":
                data["LOC"].append(span.normal)
        phrase = phrase.lower()
        match_lang = None
        for key, value in self.language_dict.items():
            match_lang = find_near_matches(key, phrase, max_l_dist=0)
            if match_lang:
                data["lang"] = {}
                data["lang"]["translate"] = phrase[match_lang[0].end + 1 :]
                if not data["lang"]["translate"]:
                    phrase = phrase[:match_lang[0].start - 1]
                    phrase_list = phrase.split()
                    if phrase_list[-1] == 'на':
                        del phrase_list[-1]
                        phrase = ' '.join(phrase_list)
                    data["lang"]["translate"] = phrase
                data["lang"]["language"] = value
                break
        if not match_lang:
            value, key = None, None
        if not data["LOC"]:
           del data["LOC"]
        if not data:
            return None
        return data


if __name__ == "__main__":
    exp1 = EntityParser()
    print(exp1.get_answer("перевод курсы по питону на английский"))
