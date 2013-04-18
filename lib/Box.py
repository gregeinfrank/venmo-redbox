#import MySQLdb

# db = MySQLdb.connect(host="localhost",
#                      user="root",
#                      passwd="venmo",
#                      db="venmo_redbox")
import time
import datetime
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

    def rent_for(self, user, steal_if_taken=False):
        if self.owner and self.owner != user and self.expiresAt > int(time.time()) and not steal_if_taken:
#            ascii_print("DOH!")
            print "%s already has box %s!" % (self.owner.name, self.boxName)
            print "This rental expires at:"
            print(datetime.datetime.fromtimestamp(self.expiresAt).strftime('%Y-%m-%d %H:%M:%S'))
            answer = raw_input("Would you like to steal from %s? [Y/N]" % self.owner.name)
            if answer == 'y' or answer == 'Y':
                self.rent_for(user, steal_if_taken=True)
        else:
            #TODO: If you're stealing, display that.
            self.owner = user
            self.expiresAt = int(time.time() + 3600) # Expire in one hour
            self.save()
            print "You now own %s for the next hour! \"Sick Set\"!!!!" % self.boxName

    def print_owner(self):
        if self.owner:
            if self.owner.picture:
                print self.owner.picture
            else:
#                ascii_print(self.owner.name)
                print "%s is the current master of %s" % (self.owner.name, self.boxName)
        else:
            print "Nobody owns box %s" % self.boxName
