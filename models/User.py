from models.Consultant import Consultant


class User:
    def __init__(self):
        # self.pid = consultant.get_id()
        self.name = ""
        self.phone = ""
        self.month = 1
        self.day = 1

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_phone(self, phone):
        self.phone = phone

    def get_phone(self):
        return self.phone

    def set_month(self, month):
        self.month = month

    def get_month(self):
        return self.month

    def set_day(self, day):
        self.day = day

    def get_day(self):
        return self.day
