#!/usr/bin/python3
# TODO: Update to allow: show, create, destroy, all - used with User (for number 7)

import cmd
import sys
from models.base_model import BaseModel
from models import storage


class ShellPrompt(cmd.Cmd):
    intro = 'Welcome to the HBnB shell. Type help or ? to list commands.'
    prompt = '(hbnb) '

    def do_create(self, args):
        new = BaseModel()
        new.save()
        print("{}".format(new.id))

    def do_show(self, args):
        args = args.split()
        if error_checking(len(args)):
            return
        item = get_instance(args[1])
        if item:
            if not usable_class(args[0]):
                print("** class doesn't exist **")
                return
            print("{}".format(item)) 
        # ADD How do we check if no class exists?
        # If the class name doesn't exist, print ** class doesn't exist **

    def do_destroy(self, args):
        args = args.split()
        if error_checking(len(args)):
            return
        item = get_instance(args[1])
        if item:
            if not usable_class(args[0]):
                print("** class doesn't exist **")
                return
            del(storage.all()[args[1]])
            storage.save()

    def do_all(self, args):
        args = args.split()
        l = []
        if len(args) < 1:
            dbdict = storage.all()
            for item, _ in dbdict.items():
                l.append(str(dbdict[item]))
            print("{}".format(l))
        else:
            if not usable_class(args[0]):
                print("** class doesn't exist **")
                return
            dbdict = storage.all()
            for item, _ in dbdict.items():
                if dbdict[item].__class__.__name__ == args[0]:
                    l.append(str(dbdict[item]))
            print("{}".format(l))

    def do_update(self, args):
        args = args.split()
        if error_checking(len(args)):
            return
        if not usable_class(args[0]):
            print("** class doesn't exist **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        item = get_instance(args[1])
        if item:
            setattr(item, args[2], args[3])
            storage.save()

    def do_quit(self, args):
        """Quits the program."""
        raise SystemExit

    def do_EOF(self, args):
        """Reached EOF"""
        print('')
        raise SystemExit

def error_checking(n):
    if n < 1:
        print("** class name missing **")
        return 1
    elif n < 2:
        print("** instance id missing **")
        return 1
    return 0

def get_instance(ID):
    try:
        item = storage.all()[ID]
    except:
        print("** no instance found **")
        return None
    return item

def usable_class(a_class):
    for i in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
        if i == a_class:
            return 1
    return 0

if __name__ == '__main__':
    ShellPrompt().cmdloop()
