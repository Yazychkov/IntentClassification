from random import choice
from skill import Skill
from utils import get_data_path
import os

class HumorIntent(Skill):
    def __init__(self):
        self.data = list()
        self.load_data()

    def load_data(self) -> None:
        with open(os.path.join(get_data_path(), 'anek_fixed.sql'), "r", encoding="Windows-1251") as file:
            for line in file:
                self.data.append(line)

    def get_answer(self, phrase, context=None) -> str:
        return choice(self.data)


if __name__ == "__main__":
    joke1 = HumorIntent()
    print(joke1.get_answer())
