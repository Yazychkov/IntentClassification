from Matcher import Matcher


from intent.humor import HumorIntent
from intent.weather import WeatherIntent
from intent.video import VideoIntent
from intent.calculator import CalcIntent
from intent.translator import TranslatorIntent
from intent.location import LocationIntent
from intent.search import SearchIntent

class Skillserver:
    def __init__(self):
        self.matcher = Matcher()
        self.intent_dict = {
            "weather": WeatherIntent,
            "video": VideoIntent,
            "calculator": CalcIntent,
            "translator": TranslatorIntent,
            "search": SearchIntent,
            "location": LocationIntent,
            "humor": HumorIntent   # с () - объект, без () - класс
        }

    def check_intent(self, text):
        if text in self.intent_dict:
            return self.intent_dict[text]

    def get_answer(self, chat_id, phrase) -> str:
        res = self.matcher.match(phrase)
        intent_result = self.check_intent(res)
        return intent_result


if __name__ == "__main__":
    exp1 = Skillserver()
    print(exp1.check_intent('humor'))
    print(exp1.get_answer('humor'))
