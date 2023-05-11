#!/usr/bin/python3
"""defines FileStorage class"""
import json, os
from models.base_model import BaseModel


class FileStorage():
    """FileStorage Class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """All Objects"""
        self.reload()
        return FileStorage.__objects

    def new(self, obj):
        """sets the object instance to __objects with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes the python objects to the JSON file class.__file_path"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            dictionary = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(dictionary, f)

    def reload(self):
        """Reload JSON objects in file to Python objects"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                print(obj_dict)
                loaded_objects = {}
                for k, v in obj_dict.items():
                    cls_name = globals()[v['__class__']]
                    loaded_objects[k] = cls_name(**v)
                FileStorage.__objects = loaded_objects
        else:
            return
