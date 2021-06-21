from natasha import (
    Segmenter,
    MorphVocab,
    NewsEmbedding,
    NewsMorphTagger,
    NewsNERTagger,
    Doc
)
from skill import Skill



class EntityParser(Skill):
    def __init__(self):
        self.segmenter = Segmenter()
        self.morph_vocab = MorphVocab()
        emb = NewsEmbedding()
        self.morph_tagger = NewsMorphTagger(emb)
        self.ner_tagger = NewsNERTagger(emb)
    
    def load_data(self) -> None:
        pass
    
    
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
        return data