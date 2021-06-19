from matcher import Matcher


from skills.humor import HumorIntent
from skills.weather import WeatherIntent
# from skills.video import VideoIntent
# from skills.calculator import CalcIntent
# from skills.translator import TranslatorIntent
# from skills.location import LocationIntent
# from skills.search import SearchIntent
from skills.entity_parser import EntityParser

class Skillserver:
    def __init__(self):
        self.matcher = Matcher()
        self.parser = EntityParser()
        self.intent_dict = {
             "weather": WeatherIntent(),
            # "video": VideoIntent(),
            # "calculator": CalcIntent(),
            # "translator": TranslatorIntent(),
            # "search": SearchIntent(),
            # "location": LocationIntent(),
            "humor": HumorIntent(),
        }

    def check_intent(self, text):
        return self.intent_dict.get(text)

    def get_answer(self, phrase, context=None ) -> str:
        context = self.parser.get_answer(phrase)
        res = self.matcher.match(phrase)
        intent_result = self.check_intent(res)
        intend_do = intent_result.get_answer(phrase, context)
        return intend_do


if __name__ == "__main__":
    exp1 = Skillserver()
    print(exp1.get_answer("погода в мск"))
