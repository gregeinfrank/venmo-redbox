import sys
import getpass
import constants
from Box import Boxes
from User import Users

def setUser():
    whoami = getpass.getuser()
    me = Users.get_user_by_name(whoami)
    if not me:
        # TODO: set the picture
        me = Users.create(name=whoami)
    return me

def steal(boxName):
    box = Boxes.get_box_by_name(boxName=boxName)
    if box:
        box.rent_for(this_user, steal_if_taken=True)
    else:
        print "WTF? No comprendo %s" % boxName

def rent(boxName):
    box = Boxes.get_box_by_name(boxName=boxName)
    if box:
        box.rent_for(this_user)
    else:
        print "Unkown box: %s" % boxName

def who(boxName):
    box = Boxes.get_box_by_name(boxName=boxName)
    if box:
        box.print_owner()
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
    elif command == 'steal':
        if len(args) < 1:
            print "What are you lookin' to steal today?"
            return
        steal(args[0])
    else:
        print constants.HELP_TEXT

this_user = setUser()
main(*sys.argv)
