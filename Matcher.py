import json


class Matcher:
    def load_data(self):
        with open("test.txt", 'r') as file:
            data = json.load(file)
            return data

    def match(self, phrase, context=None):
        if phrase in self.load_data():
            intent_name = phrase
            return intent_name
        else:
            return None

if __name__ == "__main__":
    exp = Matcher()
    print(exp.match('humor'))