from natasha import (
    Segmenter,
    MorphVocab,
    NewsEmbedding,
    NewsMorphTagger,
    NewsNERTagger,
    AddrExtractor,
    Doc
)


class EntityParser:
    def __init__(self):
        self.segmenter = Segmenter()
        self.morph_vocab = MorphVocab()
        self.addr_extractor = AddrExtractor(self.morph_vocab)
        emb = NewsEmbedding()
        self.morph_tagger = NewsMorphTagger(emb)
        self.ner_tagger = NewsNERTagger(emb)
    
    def load_data(self) -> None:
        pass
    
    
    def get_answer(self, phrase: str):
        self.replica = phrase.title()
        self.doc = Doc(self.replica)
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
        if not data["LOC"]:
            match = self.addr_extractor.find(self.replica)
            if match:
                city = self.replica[match.start : match.stop]
                for token in self.doc.tokens:
                    token.lemmatize(self.morph_vocab)
                    if token.text == city:
                        data["LOC"].append(token.lemma.title())
        return data
