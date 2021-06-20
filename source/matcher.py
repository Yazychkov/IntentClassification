import json
from utils import get_data_path
import os


class Matcher:
    def __init__(self):
        self.data = dict()
        self.load_data()

    def load_data(self):
        with open(os.path.join(get_data_path(), "skill_phrases.json"), "r", encoding='utf-8') as file:
            self.data = json.load(file)

    def match(self, phrase, context=None):
        return self.data.get(phrase)


if __name__ == "__main__":
    exp = Matcher()
    print(exp.match("humor"))
