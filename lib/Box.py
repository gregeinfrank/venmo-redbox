#import MySQLdb

# db = MySQLdb.connect(host="localhost",
#                      user="root",
#                      passwd="venmo",
#                      db="venmo_redbox")

from datetime import datetime
from peewee import (CharField, TimeField, DoesNotExist, ForeignKeyField)
from base import BaseModel
from User import Users

class Boxes(BaseModel):
    boxName = CharField()
    owner = ForeignKeyField(Users, null=True, default = None)
    lastModified = TimeField(default = datetime.now())

    @classmethod
    def get_box(klass, boxName):
        box = None
        try:
            box = klass.get(klass.boxName == boxName)
        except DoesNotExist:
            return None
        return box
