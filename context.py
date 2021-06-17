import json


class Context:
    def check_user(self, chat_id: int, name: str):
        data_dict = {"{}".format(chat_id): "{}".format(name)}
        with open("user_list.json", "r+") as file:
            data = json.load(file)
            if chat_id in data:
                file.seek(0)
            else:
                data.update(data_dict)
                file.seek(0)
                json.dump(data, file)
                file.truncate()


if __name__ == "__main__":
    exp = Context()
    exp.check_user(12456463, 'fsfds')