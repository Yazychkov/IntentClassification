import json


class Matcher:
    def __init__(self):
        self.load_data()

    def load_data(self):
        with open("test.json", "r") as file:
            self.data = json.load(file)

    def match(self, phrase):
        if phrase in self.data:
            intent_name = phrase
            return intent_name
        else:
            return None


if __name__ == "__main__":
    exp = Matcher()
    print(exp.match("humor"))
