#!/usr/bin/python3

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
        if len(args) < 1:
            print("** class name missing **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        try:
            print(storage.all()[args[1]])
        except:
            print("** no instance found **")
        # ADD How do we check if no class exists?
        # If the class name doesn't exist, print ** class doesn't exist **

    def do_destroy(self, args):
        print("We are destroying")

    def do_all(self, args):
        print("We are in all")

    def do_update(self, args):
        print("We are updating")

    def do_quit(self, args):
        """Quits the program."""
        raise SystemExit

    def do_EOF(self, args):
        """Reached EOF"""
        print('')
        raise SystemExit

if __name__ == '__main__':
    ShellPrompt().cmdloop()
