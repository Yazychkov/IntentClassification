import os
import json
import nmslib
import numpy as np
from utils import get_data_path
from embedder_bert import Embedder
import pprint


class Approximator:
    def __init__(self) -> None:
        self.bert = Embedder()

        self.text = list()
        self.phrases = np.ndarray
        self.matcher = dict()

        self.load_data()
        self.create_vectors()
        self.matching_phrases_and_vectors()

        self.index = nmslib.init(space="cosinesimil", method="hnsw")
        self.index.addDataPointBatch(self.phrases)
        self.index.createIndex()

    def load_data(self):
        with open(
            os.path.join(get_data_path(), "skill_phrases.json"), "r", encoding="UTF-8"
        ) as file:
            phrases = json.load(file)
            self.text = list(phrases.keys())
            self.text_intent = list(phrases.values())

    def create_vectors(self) -> np.ndarray:
        self.phrases = self.bert.compute_embeddings(self.text)

    def matching_phrases_and_vectors(self):
        self.matcher = {key: value for key, value in enumerate(self.text)}

    def load_to_bert(self, phrase):
        phrase_list = list()
        phrase_list.append((phrase))
        vector = self.bert.compute_embeddings(phrase_list)
        neighbours = self.index.knnQueryBatch(vector, k=3, num_threads=1)
        neighbours_list_index = neighbours[0][0][0].item()
        if neighbours_list_index in self.matcher:
            return self.matcher.get(neighbours_list_index)
        else:
            return "бот не может распознать ваши намерения"


if __name__ == "__main__":
    exp = Approximator()
    pprint.pprint(exp.load_to_bert("переведи на испанский"))
