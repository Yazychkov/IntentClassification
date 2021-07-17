import urllib.request
from urllib.parse import quote
from source.skill import Skill
import re


class VideoIntent(Skill):
    def __init__(self):
        self.data = list()
        self.res_data = list()
        self.search_query_link = "https://www.youtube.com/results?search_query="
        self.video_link = "https://www.youtube.com/watch?v="
        self.max_id_video_link = 11
        self.count_search_video = 3

    def load_data(self) -> None:
        pass

    def get_custom_sim(self, phrase) -> float:
        pass

    def get_answer(self, phrase, context=None) -> str:
        request = self.search_query_link + quote(phrase)
        html = urllib.request.urlopen(request).read().decode("cp1251", errors="ignore")
        match = re.findall('\?v\=(.+?)"', html)
        if match is not None:
            for link in match:
                if len(link) <= self.max_id_video_link:
                    self.data.append(link)
        if not self.data:
            self.res_data.append("Проверьте правильность ввода данных")
        else:
            for link in self.data[: self.count_search_video]:
                self.res_data.append(self.video_link + link)
        res_string = " ".join(self.res_data)
        self.res_data.clear(), self.data.clear()
        return res_string


if __name__ == "__main__":
    video1 = VideoIntent()
    print(video1.get_answer("как построить дом"))
    print(video1.get_answer("про котов"))
