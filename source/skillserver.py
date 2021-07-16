from source.matcher import Matcher


from source.skills.humor import HumorIntent
from source.skills.weather import WeatherIntent
from source.skills.video import VideoIntent
from source.skills.translate import TranslatorIntent

# from skills.calculator import CalcIntent
# from skills.location import LocationIntent
# from skills.search import SearchIntent
from source.entity_parser import EntityParser


class Skillserver:
    def __init__(self):
        self.matcher = Matcher()
        self.parser = EntityParser()
        self.intent_dict = {
            "weather": WeatherIntent(),
            "video": VideoIntent(),
            # "calculator": CalcIntent(),
            "translate": TranslatorIntent(),
            # "search": SearchIntent(),
            # "location": LocationIntent(),
            "humor": HumorIntent(),
        }

    def check_intent(self, text):
        return self.intent_dict.get(text)

    def get_answer(self, phrase, context=None) -> str:
        res = self.matcher.match(phrase)
        print(res)
        intent_result = self.check_intent(res)
        print(intent_result)
        if intent_result:
            if not context:
                context = dict()
            res_parser = self.parser.get_answer(phrase)
            if res_parser:
                context["res_parser"] = res_parser
            intend_do = intent_result.get_answer(phrase, context)
            return intend_do
        else:
            return "Я не смог распознать ваше намерение, пожалуйста, попробуйте переформулировать"


if __name__ == "__main__":
    exp1 = Skillserver()
    print(exp1.get_answer("видео на ютуб про кота"))
