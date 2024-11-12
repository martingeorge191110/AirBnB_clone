#!/usr/bin/python3
"""module of creating the CMD class"""

import cmd
import sys

class My_Interpreter(cmd.Cmd):
    """Custom command line interpreter for 
    Airbnb project"""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Handle EOF to exit the program"""
        return True
    
    def do_quit(self, line):
        """quit the interpreter"""
        return True
    
    def emptyline(self):
        """pass the emptyline with doing nothing"""
        pass

if __name__ == '__main__':
    shell = My_Interpreter()
    if len (sys.argv) == 1:
        shell.cmdloop()
    else:
        input_data = sys.argv.read()
        for command in input_data.splitlines():
            shell.onecmd(command)
        
