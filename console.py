#!/usr/bin/python3

import cmd
import sys


class ShellPrompt(cmd.Cmd):
    intro = 'Welcome to the HBnB shell. Type help or ? to list commands.\n'
    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quits the program."""
        raise SystemExit

    def do_EOF(self, args):
        """Reached EOF"""
        return True

if __name__ == '__main__':
    ShellPrompt().cmdloop()
