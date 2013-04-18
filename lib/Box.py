#import MySQLdb

# db = MySQLdb.connect(host="localhost",
#                      user="root",
#                      passwd="venmo",
#                      db="venmo_redbox")

import constants
from peewee import (MySQLDatabase, Model, CharField, TimeField, IntegerField, DoesNotExist)

mysql_db = MySQLDatabase(constants.DB_NAME, user=constants.DB_USER, passwd=constants.DB_PASSWORD)
mysql_db.connect()

class Boxes(Model):
    id = IntegerField(primary_key=True)
    boxName = CharField()
    owner = IntegerField(null=True)
    lastModified = TimeField()

    class Meta:
        database = mysql_db

    @classmethod
    def get_box(klass, boxName):
        box = None
        try:
            box = klass.get(klass.boxName == boxName)
        except DoesNotExist:
            return None
        return box
