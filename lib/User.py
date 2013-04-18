import constants
from peewee import (MySQLDatabase, Model, IntegerField, CharField, TimeField, DoesNotExist)

mysql_db = MySQLDatabase(constants.DB_NAME, user=constants.DB_USER, passwd=constants.DB_PASSWORD)
mysql_db.connect()

class Users(Model):
    id = IntegerField(primary_key=True)
    name = CharField()
    picture = CharField()
    lastModified = TimeField()

    class Meta:
        database = mysql_db

    @classmethod
    def get_user_by_id(klass, id):
        user = None
        try:
            user = klass.get(klass.id == id)
        except DoesNotExist:
            return None
        return user
