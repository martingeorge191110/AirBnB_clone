#!/usr/bin/python3
"""module of creating the CMD class"""

import cmd

class My_Interpreter(cmd.Cmd):

    prompt = '(hbnb) '

    def do_EOF(self, line):
        """End of input for a command or program 
        that is reading data from the standard input"""
        return True
    
    def do_quit(self, line):
        """quit the interpreter"""
        return True
    
    def postloop(self):
        print

if __name__ == '__main__':
    My_Interpreter().cmdloop()
