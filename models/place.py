#!/usr/bin/python3
""" shebang line - defines where the interpreter is located """
from models.base_model import BaseModel
""" import moduls """


class Place(BaseModel):
    """ Main class to manage Places, it inherited of BaseModel """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
