import json
from utils import get_data_path
from approximate_nn import Approximator
import os


class Matcher:
    def __init__(self):
        self.data = dict()
        self.load_data()

        self.knn = Approximator()

    def load_data(self):
        with open(
            os.path.join(get_data_path(), "skill_phrases.json"), "r", encoding="utf-8"
        ) as file:
            self.data = json.load(file)

    def match(self, phrase, context=None):
        if self.knn.load_to_bert(phrase) in self.data:
            return self.data.get(self.knn.load_to_bert(phrase))
        else:
            return False


if __name__ == "__main__":
    exp = Matcher()
    print(exp.match("анекдот"))

