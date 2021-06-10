import json


class Context:
    def check_user(self, chat_id: int, name: str):
        data_dict = {'{}'.format(chat_id): '{}'.format(name)}
        with open('user_list.json', 'r+') as file:
            data = json.load(file)
            for key, value in file:
                if key == chat_id:
                    break
            data.update(data_dict)
            file.seek(0)
            json.dump(data, file)

# check_user(124455514, 'ssdaf')





