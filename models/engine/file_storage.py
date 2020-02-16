#!/usr/bin/python3
import json

class FileStorage:
    """ serializes instances to a JSON file and deserializes JSON file to instances """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        """ adds a new object to __objects dictionary """
        self.__objects[obj.id] = obj

    def save(self):
        """ uses the __objects dictionary to serialize its objects and save them into a JSON file """
        for key, value in self.__objects.items():
            with open(self.__file_path, "a") as f:
                f.write(json.dumps(value))

    def reload(self):
        with open(self.__file_path, "r") as f:
            for i in f:
                pobj = json.loads(i.read())
                self.__objects[pobj.id] = pobj
