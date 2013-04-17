#import MySQLdb
#from peewee import *
import peewee

# db = MySQLdb.connect(host="localhost",
#                      user="root",
#                      passwd="venmo",
#                      db="venmo_redbox")

mysql_db = peewee.MySQLDatabase('venmo_redbox', user="root", passwd="venmo")
mysql_db.connect()

class Boxes(peewee.Model):
    id = peewee.IntegerField(primary_key=True)
    boxName = peewee.CharField()
    owner = peewee.IntegerField(null=True)
    lastModified = peewee.TimeField()

    class Meta:
        database = mysql_db
