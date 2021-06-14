import requests
import entity_parser
import dictionary
import settings


class WeatherIntent:
    def translit(self, city_name: str):
        for key in city_name:
            city_name = city_name.replace(key, dictionary.letters_dict[key])
        return city_name

    def det_weather(self, replica: str):

        replica = entity_parser.EntityParser(text)
        location = replica.parser()
        city = location["LOC"]
        if not city:
            return "В вашей фразе я не смог распознать город"
        else:
            city_name = city[0]
            letter_city_name = city_name[0]
            if dictionary.city_dict[letter_city_name].get(city_name):
                city_name = dictionary.city_dict[letter_city_name][city_name]
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
    text = "сколько градусов в мск"
    print(test.det_weather(text))
