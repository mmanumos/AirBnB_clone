#!/usr/bin/python3
""" shebang line - defines where the interpreter is located """
from datetime import datetime
from uuid import uuid4
""" import moduls """


class BaseModel:
    """ defines all common attributes/methods for other classes """

    def __init__(self, *args, **kwargs):
        """" constructor """
        if kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = kwargs.get(key)
                if key == "created_at":
                    self.created_at = datetime.strptime(kwargs.get(key),'%Y-%m-%dT%H:%M:%S.%f')
                if key == "updated_at":
                    self.update_at = datetime.strptime(kwargs.get(key),'%Y-%m-%dT%H:%M:%S.%f')
                if key == "my_number":
                    self.my_number = kwargs.get(key)
                if key == "name":
                    self.name = kwargs.get(key)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

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
        my_dict['created_at'] = (self.created_at).isoformat()
        my_dict['updated_at'] = (self.updated_at).isoformat()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['id'] = self.id
        return(my_dict)
