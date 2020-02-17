#!/usr/bin/python3
""" shebang line - defines where the interpreter is located """
import cmd
""" import moduls """


class HBNBCommand(cmd.Cmd):
    """ class with methods to work into the commands line """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, line):
        """ EOF command to exit the program """
        return True

    def emptyline(self):
        """ When the comand line is empty and it's typed """
        pass

""" Executed the loop for Promp by default """
HBNBCommand().cmdloop()
