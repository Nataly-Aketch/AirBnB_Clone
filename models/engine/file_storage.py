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
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            dictionary = {k: v.to_dict() for k,v in FileStorage.__objects.items()}
            json.dump(dictionary, f)
    
    def reload(self):
        """Reload JSON objects in file to Python objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
