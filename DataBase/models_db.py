from peewee import *

db = MySQLDatabase(
    host='127.0.0.1',
    user='root',
    password='',
    database='bot'
)
db.connect()


class Consultant(Model):
    id = AutoField()
    name = CharField()
    phone = CharField()
    chat_id = IntegerField()
    all_message = TextField()
    birthday_message = TextField()

    class Meta:
        db_table = 'consultants'
        database = db


class Client(Model):
    pid = ForeignKeyField(Consultant, related_name='clients')
    name = CharField()
    phone = CharField()
    chat_id = IntegerField()
    date = DateField()

    class Meta:
        db_table = 'client'
        database = db


Consultant.create_table()
Client.create_table()
db.close()