from peewee import (IntegerField, CharField, TimeField, DoesNotExist)
from Base import BaseModel

class Users(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField()
    picture = CharField()
    lastModified = TimeField()

    @classmethod
    def get_user_by_id(klass, id):
        user = None
        try:
            user = klass.get(klass.id == id)
        except DoesNotExist:
            return None
        return user
