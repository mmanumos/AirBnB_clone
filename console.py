#!/usr/bin/python3
""" shebang line - defines where the interpreter is located """
import cmd
""" import moduls """

class hbnbShell(cmd.Cmd):
    """ Command processor """
    prompt = '(hbnb)'

    # ----- basic hbnd commands -----
    def do_EOF(self, arg):
        """ EOF hbnbShell """
        return True

    # ----- basic hbnd commands -----
    def do_quit(self, arg):
        """ Quit hbnbShell """
        return True

if __name__ == '__main__':
    hbnbShell().cmdloop()
