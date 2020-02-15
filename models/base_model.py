#!/usr/bin/python3
""" shebang line - defines where the interpreter is located """
from datetime import datetime
from uuid import uuid4
""" import moduls """


class BaseModel:
    """ defines all common attributes/methods for other classes """
    def __init__(self, *args, **wkargs):
        """" constructor """
        name = ""
        my_number = 0

    def __str__(self):
        """ define str output """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.name, self.my_number))
