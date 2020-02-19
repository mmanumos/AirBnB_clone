#!/usr/bin/python3
""" shebang line - defines where the interpreter is located """
from models.base_model import BaseModel
""" import moduls """


class User(BaseModel):
    """ Main class to manage Users, it inherited of BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
