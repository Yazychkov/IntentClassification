from class_Matcher import Matcher

from WeatherIntent import Weatherintent
from VideoIntent import Videointent
from CalcIntent import Calcintent
from TranslatorIntent import Translatorintent
from SearchIntent import Searchintent
from LocationIntent import Locationintent
from HumorIntent import Humorintent

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
        for key in intent_dict:
            if text == key:
                return intent_dict[key]

    def get_answer(self, chat_id, phrase):
        # chat_id = TelegramChecker()  #получение chat_id из класса чекер
        # res = chat_id.get_chat_id(update, context) #создание экземпляра класса
        # update.message.reply_text(res, text=phrase)

        # блок наследования из другого класса

        phrase = ('ответ от скиллсервера {}'.format())
        return phrase








