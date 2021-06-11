import random
import class_Skill as Skill


class HumorIntent(Skill):
    def get_random_joke(self):
        with open("../anek_fixed.sql", "r", encoding="Windows-1251") as file:
            random_joke = random.randint(0, 130263)
            cnt = 0
            for joke in file:
                cnt += 1
                if cnt == random_joke:
                    return joke
                    cnt = 0
            file.close()


if __name__ == "__main__":
    joke1 = HumorIntent()
