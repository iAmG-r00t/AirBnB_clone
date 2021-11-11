#!/usr/bin/python3
"""
Serializes instances to a JSON file and deserializes JSON file to instances
"""
import json
from datetime import datetime


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = type(obj).__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj
        
    def save(self):
        """
        serializes FileStroage.__objects
        """
        with open(FileStorage.__file_path, 'w+') as f:
            dictofobjs = {}
            for key, value in FileStorage.__objects.items():
                dictofobjs[key] = value.to_dict()
            json.dump(dictofobjs, f)

    def reload(self):
        """
        deserializes instances got from json file
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                dictofobjs = json.loads(f.read())
                from models.base_model import BaseModel
                for key, value in dictofobjs.items():
                    FileStorage.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass
