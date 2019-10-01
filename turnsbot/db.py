from mongoengine import Document, StringField, ListField, ReferenceField, DateField


class User(Document):
    chat_id = StringField(required=True)
    first_name = StringField(required=True)
    full_name = StringField(required=True)


class Turn(Document):
    date = DateField(required=True)
    user = ReferenceField(User)


class Task(Document):
    name = StringField(required=True)
    turns = ListField(Turn)
