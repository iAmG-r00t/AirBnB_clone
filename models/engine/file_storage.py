#!/usr/bin/python3
"""
Serializes instances to a JSON file and deserializes JSON file to instances
"""
import json


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = type(obj).__name__ + '.' + str(obj.id)
        FileStorage.__objects[key] = obj.__str__()
        
    def save(self):
        objstr = json.dumps(FileStorage.__objects)
        with open(FileStorage.__file_path, 'w+') as f:
            f.write(objstr)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as f:
                FileStorage.__objects = json.loads(f.read())
        except FileNotFoundError:
            pass
