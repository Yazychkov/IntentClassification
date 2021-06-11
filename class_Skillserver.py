from class_Matcher import Matcher

from IntentClassification.intent.humor import HumorIntent

class Skillserver:
    def __init__(self):
        self.matcher = Matcher()
        self.telegramchecker = TelegramChecker()

    def check_intent(self, text):
        intent_dict = {
            'weather': WeatherIntent(),
            'video': VideoIntent(),
            'calculator': CalcIntent(),
            'translator': TranslatorIntent(),
            'search': SearchIntent(),
            'location': LocationIntent(),
            'humor': HumorIntent()
        }
        if text in intent_dict.keys():
            return intent_dict[text]

    def get_answer(self, chat_id, phrase): #chat_id?
        search = Matcher()
        phrase = ('ответ от скиллсервера {}'.format(search.match(phrase)))
        return phrase
