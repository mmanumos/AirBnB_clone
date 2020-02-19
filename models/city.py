#!/usr/bin/python3
""" shebang line - defines where the interpreter is located """
from models.base_model import BaseModel
""" import moduls """


class City(BaseModel):
    """ Main class to manage Cities, it inherited of BaseModel """
    state_id = ""
    name = ""
