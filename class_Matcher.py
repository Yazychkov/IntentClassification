
import json

class Matcher:
    def __init__(self, data):
        self.data = data
        # self.skillserver = Skillserver()

    def load_data(self):
        with open('test.json') as file:
            self.data = json.load(file)
            return self.data

    def match(self, input_phrase):
        dict_data = json.loads(self.data)
        for key in dict_data:
            if input_phrase == key:
                intent_name = dict_data[key]
                return intent_name
            else:
                return None

