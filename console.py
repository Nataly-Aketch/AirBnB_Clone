#!/usr/bin/python3
"""this program contains the entry point of the command interpreter"""
import cmd
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


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
        if new_line[0] not in self.cls_list:
            print("** class doesn't exist **")
        if not new_line[1]:
            print("** instance id missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
