from googletrans import Translator
from source.utils import get_data_path
import json
import os
from source.skill import Skill

class TranslatorIntent(Skill):
    def __init__(self):
        self.tr = Translator()
        self.lang_reversed = dict()
        self.load_data()

    def load_data(self) -> None:
        with open(os.path.join(get_data_path(), "languages.json"), 'r') as file:
            lang = json.load(file)
            self.lang_reversed = {value: key for key, value in lang.items()}

    def get_custom_sim(self, phrase) -> float:
        pass

    def get_answer(self, phrase, context=None) -> str:
        'фраза - перевод на какой язык: "я люблю перевод на немецкий"'
        destination_language = str()
        phrase_list = phrase.lower().split()
        phrase_for_leng = phrase_list[-1:]
        del phrase_list[-2:]
        phrase_str = ' '.join(phrase_list)
        inter_result = self.tr.translate(phrase_for_leng[0], dest='en')
        if inter_result.text.lower() in self.lang_reversed:
            destination_language += self.lang_reversed.get(inter_result.text.lower())
        else:
            return 'Проверьте правильность написания языка, на который вы хотите перевести'
        result = self.tr.translate(phrase_str, dest=destination_language)
        return result.text


if __name__ == "__main__":
    tr1 = TranslatorIntent()
    tr1.load_data()
    print(tr1.get_answer("перевод на испанский"))
