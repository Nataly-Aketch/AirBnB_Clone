#!/usr/bin/python3
"""defines FileStorage class"""
import json


class FileStorage():
    """FileStorage Class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """All Objects"""
        return FileStorage.__objects

    def new(self, obj):
        """New Objects"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Save an object to the file"""
        dictionary = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(dictionary, f)

    def reload(self):
        """Reload JSON objects in file to Python objects"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                obj_dict = json.load(f)
                for k, v in obj_dict.items():
                    cls_name = v['__class__']
                    new_dict[k] = eval(cls_name)(**v)
                FileStorage.__objects = new_dict
        except Exception:
            pass
