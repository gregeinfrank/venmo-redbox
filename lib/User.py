from peewee import (CharField, TimeField, DoesNotExist)
from base import BaseModel

class Users(BaseModel):
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
