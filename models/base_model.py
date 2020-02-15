#!/usr/bin/python3
""" shebang line - defines where the interpreter is located """
from datetime import datetime
from uuid import uuid4
""" import moduls """


class BaseModel:
    """ defines all common attributes/methods for other classes """

    my_number = 0
    name = ""

    def __init__(self):
        """" constructor """
        self.id = str(uuid4())
        self.created_at = (datetime.now()).isoformat()
        self.update_at = (datetime.now()).isoformat()

    def save(self):
         """ Update the update_at"""
         self.updated_at = (datetime.now()).isoformat()


    def __str__(self):
        """ __str__ """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def to_dict(self):
        """ Returns a dictionary """
        my_dict = {}
        my_dict['my_number'] = self.my_number
        my_dict['name'] = self.name
        my_dict['created_at'] = self.created_at
        my_dict['updated_at'] = self.updated_at
        my_dict['__class__'] = self.__class__.__name__
        my_dict['id'] = self.id
        return(my_dict)
