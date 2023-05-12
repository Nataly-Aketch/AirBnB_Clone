#!/usr/bin/python3
"""this program contains the entry point of the command interpreter"""
import cmd
import re
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """command processor"""
    prompt = '(hbnb) '
    cls_list = ['BaseModel', 'State', 'City', 'User'
               'Place', 'Amenity', 'Review']

    def do_EOF(self, line):
        """End of File to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        exit()

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id"""
        if not line:
            print("** class name missing **")
        elif line not in self.cls_list:
            print("** class doesn't exist **")
        else:
            new = BaseModel()
            print(new.id)
            new.save()

    def do_show(self, line):
        """Prints the string representation of an instance based
        on the class name and id"""
        new_line = line.split()
        if not line:
            print("** class name missing **")
        elif new_line[0] not in self.cls_list:
            print("** class doesn't exist **")
        elif len(new_line) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(new_line[0], new_line[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])
    
    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        input = line.split()
        if not line:
            print("** class name missing **")
        else:
            if input[0] not in self.cls_list:
                print("** class doesn't exist **")
            elif len(input) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(input[0], input[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()
    
    def do_all(self, line):
        """Prints all string representation of all instances based or not in the class name"""
        obj_list = []
        if line != "":
            input = line.split()
            if input[0] not in self.cls_list:
                print("** class doesn't exist **")
            else:
                for key, value in storage.all().items():
                    if type(value).__name__ == input[0]:
                        obj_list.append(str(value))
                print(obj_list)
        else:
            for key, value in storage.all().items():
                obj_list.append(str(value))
            print(obj_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        input = line.split()
        if len(input) < 4:
            print("update <class name> <id> <attribute name> \"<attribute value>\"")
        else:
            if len(input) > 4:
                print("Only one attribute can be updated at a time")
            key = "{}.{}".format(input[0], input[1])
            if hasattr(storage.all()[key], input[2]):
                cast = type(getattr(storage.all()[key], input[2]))
                value = cast(input[3])
                






            
            


if __name__ == '__main__':
    HBNBCommand().cmdloop()
