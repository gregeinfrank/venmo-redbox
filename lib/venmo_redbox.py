import sys
from Box import Boxes
from User import Users

def main(script, command, *args):
    if command == 'who':
        if len(args) < 1:
            print "Input what box you want to ask about"
            return
        boxName = args[0]
        box = Boxes.get_box(boxName=boxName)
        if box:
            print "We found box %s" % boxName
            if box.owner:
                owner = Users.get_user_by_id(box.owner)
                print "%s is the current master of %s" % (owner.name, boxName)
            else:
                print "Nobody owns box %s" % boxName
        else:
            print "No box named %s.  Better luck next time!" % boxName

main(*sys.argv)
