import requests
import json
from source.skill import Skill
from source.utils import get_data_path
import os


class WeatherIntent(Skill):
    def __init__(self):
        self.city_list = dict()
        self.letters_dict = dict()
        self.load_data()

    def load_data(self) -> None:
        with open(
            os.path.join(get_data_path(), "city_list.json"), "r", encoding="utf-8"
        ) as f:
            self.city_list = json.load(f)
        self.city_dict = {
            loc: el_list[1] for el_list in self.city_list for loc in el_list[0]
        }
        with open(
            os.path.join(get_data_path(), "dictionary_letters.json"),
            "r",
            encoding="utf-8",
        ) as f:
            self.letters_dict = json.load(f)

    def translit(self, city_name: str):
        city_name = "".join(
            [key.replace(key, self.letters_dict[key]) for key in city_name]
        )
        return city_name

    def get_answer(self, phrase, context = None) -> str:
        if not context or not context["res_parser"].get('LOC'):
            return "В вашей фразе я не смог распознать город"
        city = context["res_parser"]["LOC"]
        city_name = None
        for location in city:
            if self.city_dict.get(location) and (city_name is None):
                city_name = self.city_dict[location]
            elif self.city_dict.get(location):
                return "В вашей фразе я распознал несколько городов"
        if not city_name:
            return "В вашей фразе я не смог распознать город"
        city = city_name
        city_name = self.translit(city_name)
        try:
            res = requests.get(
                "http://api.openweathermap.org/data/2.5/weather",
                params={
                    "q": city_name,
                    "units": "metric",
                    "lang": "ru",
                    "APPID": os.environ['API_KEY_WEATHER'],
                },
            )
            data = res.json()
            answer = (
                "Город: "
                + str(city)
                + "; На улице "
                + str(data["weather"][0]["description"])
                + "; Температура "
                + str(data["main"]["temp"])
                + "; Ощущается как "
                + str(data["main"]["feels_like"])
            )
            return answer
        except Exception as e:
            if data["cod"] == "404":
                return f"Город {city} не найден."
            else:
                return "Технические неполадки, пожалуйста, попробуйте позднее."


if __name__ == "__main__":
    test = WeatherIntent()
    text = "погода в москве"
    context = {}
    context["res_parser"] = {'LOC': ['Москва']}
    print(test.get_answer(text,context))
