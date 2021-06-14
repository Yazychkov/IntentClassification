import random
from IntentClassification.Skill import Skill


class HumorIntent(Skill):
    def __init__(self):
        self.file = open("anek_fixed.sql", "r", encoding="Windows-1251")

    def load_data(self) -> None:
        self.file

    def get_answer(self) -> str:
        random_joke = random.randint(0, 130263)
        cnt = 0
        for joke in self.file:
            cnt += 1
            if cnt == random_joke:
                return joke


if __name__ == "__main__":
    joke1 = HumorIntent()
    print(joke1.get_answer())
