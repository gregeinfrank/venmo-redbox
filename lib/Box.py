#import MySQLdb

# db = MySQLdb.connect(host="localhost",
#                      user="root",
#                      passwd="venmo",
#                      db="venmo_redbox")

from peewee import (CharField, IntegerField, DoesNotExist, ForeignKeyField)
from base import BaseModel
from User import Users

class Boxes(BaseModel):
    boxName = CharField()
    owner = ForeignKeyField(Users, null=True, default = None)
    expiresAt = IntegerField()

    @classmethod
    def get_box_by_name(klass, boxName):
        box = None
        try:
            box = klass.get(klass.boxName == boxName)
        except DoesNotExist:
            return None
        return box
