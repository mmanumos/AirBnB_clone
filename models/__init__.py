#!/usr/bin/python3
""" shebang line - defines where the interpreter is located """
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity


storage = FileStorage()
storage.reload()
