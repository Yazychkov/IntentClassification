import json


class Matcher:
    def __init__(self):
        self.data = dict()
        self.load_data()

    def load_data(self):
        with open("../data/skill_phrases.json", "r") as file:
            self.data = json.load(file)

    def match(self, phrase, context=None):
        return self.data.get(phrase)


if __name__ == "__main__":
    exp = Matcher()
    print(exp.match("humor"))
