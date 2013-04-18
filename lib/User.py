from peewee import (MySQLDatabase, Model, IntegerField, CharField, TimeField, DoesNotExist)

mysql_db = MySQLDatabase('venmo_redbox', user="root", passwd="venmo")
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
