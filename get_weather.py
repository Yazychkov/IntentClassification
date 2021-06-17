import requests
import entity_parser
import settings
import json
import dictionary_letters


class WeatherIntent:
    def __init__(self):
        with open('city_list.json', 'r', encoding='utf-8') as f:
            self.city_list = json.load(f)
        


    def load_data(self) -> None:
        self.city_dict = {loc: el_list[1] for el_list in self.city_list for loc in el_list[0]}
        

    def translit(self, city_name: str):
        for key in city_name:
            city_name = city_name.replace(key, dictionary_letters.letters_dict[key])
        return city_name

    def get_answer(self, phrase: str):

        data = entity_parser.EntityParser()
        location = data.get_answer(phrase)
        city = location["LOC"]
        if not city:
            return "В вашей фразе я не смог распознать город"
        else:
            city_name = city[0]
            if self.city_dict.get(city_name):
                city_name = self.city_dict[city_name]
                city = city_name
                city_name = self.translit(city_name)
                try:
                    res = requests.get(
                        "http://api.openweathermap.org/data/2.5/weather",
                        params={
                            "q": city_name,
                            "units": "metric",
                            "lang": "ru",
                            "APPID": settings.appid,
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
                        return (
                            "Технические неполадки, пожалуйста, попробуйте позднее.",
                        )
            else:
                return "В вашей фразе я не смог распознать город"


if __name__ == "__main__":
    test = WeatherIntent()
    test.load_data()
    text = "погода в нижнем новгороде"
    print(test.get_answer(text))
