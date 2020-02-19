#!/usr/bin/python3
""" shebang line - defines where the interpreter is located """
from models.base_model import BaseModel
""" import moduls """


class Amenity(BaseModel):
    """ Main class to manage Amenities, it inherited of BaseModel """
    name = ""
