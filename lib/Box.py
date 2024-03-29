import time
import datetime
from peewee import (CharField, IntegerField, DoesNotExist, ForeignKeyField)
from base import BaseModel
from User import Users
from utils import ascii_print

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

    def return_for(self, user):
        if self.owner and not self.is_available() and self.owner == user:
            self.owner = None
            self.expiresAt = 0
            self.save()
            ascii_print("Thank You")
        else:
            print "That was unecessary... You don't own %s" % self.boxName

    def rent_for(self, user, steal_if_taken=False):
        if not self.is_available() and self.owner != user and not steal_if_taken:
            ascii_print("DOH!")
            print "%s already has box %s!" % (self.owner.name, self.boxName)
            print "This rental expires at:"
            print(datetime.datetime.fromtimestamp(self.expiresAt).strftime('%Y-%m-%d %H:%M:%S'))

            answer = raw_input("Would you like to steal from %s? [Y/N] " % self.owner.name)
            while answer not in ['y', 'Y', 'n', 'N']: # We keep asking until they give us a "y" or "n" (case insensitive)
                answer = raw_input("Please respond [Y/N] ")
            if answer in ['y', 'Y']:
                self.rent_for(user, steal_if_taken=True)
        else:
            self.expiresAt = int(time.time() + 3600) # Expire in one hour
            if self.owner == user:
                ascii_print("Renewed")
                print "Congrats! You've extended your rental of %s for another hour! New expiration time is: %s" % (
                        self.boxName, datetime.datetime.fromtimestamp(self.expiresAt).strftime('%Y-%m-%d %H:%M:%S'))
            else:
                if not self.is_available():
                    ascii_print("SWIPE!")
                    print "You stole %s from %s" % (self.boxName, self.owner.name)
                self.owner = user
            self.save()
            print "You now own %s for the next hour! \"Sick Set\"!!!!" % self.boxName

    def print_owner(self):
        if self.is_available():
            ascii_print("All Yours")
            print "Nobody owns box %s" % self.boxName
        else:
            if self.owner.picture:
                print self.owner.picture
            else:
                ascii_print(self.owner.name)
                print "%s is the current owner of %s" % (self.owner.name, self.boxName)


    def is_available(self):
        if self.owner:
            if self.expiresAt > int(time.time()):
                return False
        return True
