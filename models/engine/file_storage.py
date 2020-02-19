#!/usr/bin/python3
""" shebang line - defines where the interpreter is located """
import json
import os.path
from ..base_model import BaseModel
""" import moduls """


class FileStorage:
    """ serializes instances to a JSON file
    and deserializes JSON file to instances """
    __file_path = "file.json"
    __objects = {}
    """ Private class attributes """

    def all(self):
        """ Public instance method that returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Public instance method that sets in __objects
        the obj with key <obj class name>.id """
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__,
                                             obj.id)] = obj.to_dict()

    def save(self):
        """ Public instance method that serializes
        __objects to the JSON file """
        with open(FileStorage.__file_path, "w") as f:
            f.write(json.dumps(FileStorage.__objects))

    def reload(self):
        """ Public instance method that deserializes
        the JSON file to __objects """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                FileStorage.__objects = json.loads(f.read())
