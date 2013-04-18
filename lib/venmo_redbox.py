import sys
from random import choice
import time
import datetime
import getpass
import urllib2
from Box import Boxes
from User import Users

def setUser():
    whoami = getpass.getuser()
    me = Users.get_user_by_name(whoami)
    if not me:
        # TODO: set the picture
        me = Users.create(name=whoami)
    return me

def ascii_print(string):
    ascii_fonts = urllib2.urlopen("http://artii.herokuapp.com/fonts_list").read().split('\n')
    font = choice(ascii_fonts)
    print font
    print urllib2.urlopen("http://artii.herokuapp.com/make?text=%s&font=%s" % (string, font)).read()

def rent(boxName):
    box = Boxes.get_box_by_name(boxName=boxName)
    if box:
        if box.owner and box.owner != this_user and box.expiresAt > int(time.time()):
            ascii_print("DOH!")
            print "%s already has box %s!" % (box.owner.name, boxName)
            print "This rental expires at:"
            print(datetime.datetime.fromtimestamp(box.expiresAt).strftime('%Y-%m-%d %H:%M:%S'))
        else:
            box.owner = this_user
            box.expiresAt = int(time.time() + 3600) # Expire in one hour
            box.save()
            print "You now own %s for the next hour! \"Sick Set\"!!!!" % boxName
    else:
        print "Unkown box: %s" % boxName

def who(boxName):
    box = Boxes.get_box_by_name(boxName=boxName)
    if box:
        print "We found box %s" % boxName
        if box.owner:
            if box.owner.picture:
                print box.owner.picture
            else:
                ascii_print(box.owner.name)
                print "%s is the current master of %s" % (box.owner.name, boxName)
        else:
            print "Nobody owns box %s" % boxName
    else:
        print "No box named %s.  Better luck next time!" % boxName

def main(script, command, *args):
    if command == 'who':
        if len(args) < 1:
            print "Wat?? Please input the box name you want to know about"
            return
        who(args[0])
    elif command == 'rent':
        if len(args) < 1:
            print "Bro, you need to specify which box you want to rent"
            return
        rent(args[0])

this_user = setUser()
main(*sys.argv)
