import json


class Context:
    def __init__(self, chat_id: int, name: str):
        self.name = name
        self.chat_id = chat_id

    def save(self, chat_id, name):
        data_dict = {"chat_id": chat_id, "name": name}
        with open("../data/user_list.json", "r+") as file:
            data = json.load(file)
            data.append(data_dict)
            file.seek(0)
            json.dump(data, file, indent=2)
            file.truncate()

    def load(self, chat_id):
        with open("../data/user_list.json", "r") as file:
            data = json.load(file)
            for people in data:
                if people["chat_id"] == chat_id:
                    return people["name"]


if __name__ == "__main__":
    exp = Context(7778, "fsfds")
    print(exp.load(7778))
