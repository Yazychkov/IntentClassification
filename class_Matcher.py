import json


class Matcher:
    def __init__(self, data):
        self.data = data

    def load_data(self):
        with open("test.json") as file:
            self.data = json.load(file)
            return self.data

    def match(self, input_phrase):
        dict_data = json.loads(self.data)
        if input_phrase in dict_data.keys():
            intent_name = dict_data[input_phrase]
            return intent_name
        else:
            return None
