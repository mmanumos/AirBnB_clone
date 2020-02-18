#!/usr/bin/python3
""" shebang line - defines where the interpreter is located """
""" contains the entry point of the command interpreter """
import cmd
""" import moduls """

class HBNBCommand(cmd.Cmd):
    """ command processor """
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ EOF command to exit the program """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
