from DataBase.models_db import Consultant as Table


class Consultant:

    def __init__(self, chat_id):
        select = Table.select().where(Table.chat_id == str(chat_id)).get()
        for item in select:
            self.id = item.id
            self.name = item.name
            self.phone = item.phone
            self.chat_id = item.chat_id
            self.all_message = item.all_message
            self.birthday_message = item.birthday_message

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone

    def get_chat_id(self):
        return self.chat_id

#   set_chat_id отсутствует, чтобы нельзя было изменить chat_id консультанта

    def get_all_message(self):
        return self.all_message

    def set_all_message(self, all_message):
        self.all_message = all_message

    def get_birthday_message(self):
        return self.birthday_message
