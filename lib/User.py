import constants
from peewee import (MySQLDatabase, Model, IntegerField, CharField, TimeField, DoesNotExist)

mysql_db = MySQLDatabase(constants.DB_NAME, constants.DB_USER, constants.DB_PASSWORD)
mysql_db.connect()

class Users(Model):
    id = IntegerField(primary_key=True)
    name = CharField()
    picture = CharField()
    lastModified = TimeField()

    class Meta:
        database = mysql_db

    @classmethod
    def get_user(klass, name):
        user = None
        try:
            user = klass.get(klass.name == name)
        except DoesNotExist:
            return None
        return user
