#!/usr/bin/python3
"""module of creating the CMD class"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Custom command line interpreter for
    Airbnb project"""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Handle EOF to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """pass the emptyline with doing nothing"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
