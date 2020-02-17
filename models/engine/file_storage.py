#!/usr/bin/python3
""" shebang line - defines where the interpreter is located """
import json
from ..base_model import BaseModel
""" import moduls """

class FileStorage:
    """ serializes instances to a JSON file and deserializes JSON file to instances """
    __file_path = "file.json"
    __objects = {}
    """ Private class attributes """

    def all(self):
        """ Public instance method that returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Public instance method that sets in __objects the obj with key <obj class name>.id """
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """ Public instance method that serializes __objects to the JSON file """
        nd = {}
        for key, value in FileStorage.__objects.items():
            nd.update({key: value.to_dict()})
            jfile = json.dumps(nd)
            with open(FileStorage.__file_path, "a") as f:
                f.write(jfile)

    def reload(self):
        """ Public instance method that deserializes the JSON file to __objects """
        md = {"BaseModel": BaseModel}
        jfile = ""
        try:
            with open(FileStorage.__file_path, "r") as f:
                jfile = json.loads(f.read())
                for i in jfile:
                    FileStorage.__objects[i] = md[jfile[i]['__class'](**jfile[i])]
        except:
            pass
