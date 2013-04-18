import constants
from peewee import (MySQLDatabase, Model)

mysql_db = MySQLDatabase(constants.DB_NAME, user=constants.DB_USER, passwd=constants.DB_PASSWORD)
mysql_db.connect()

class BaseModel(Model):

    class Meta:
        database = mysql_db
