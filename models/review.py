#!/usr/bin/python3
""" shebang line - defines where the interpreter is located """
from models.base_model import BaseModel
""" import moduls """


class Review(BaseModel):
    """ Main class to manage Reviews, it inherited of BaseModel """
    place_id = ""
    user_id = ""
    text = ""
