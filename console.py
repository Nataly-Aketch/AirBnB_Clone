#!/usr/bin/python3
"""this program contains the entry point of the command interpreter"""
from models.base_model import BaseModel
import cmd


class HBNBCommand(cmd.Cmd):
    """command processor"""
    prompt = '(hbnb) '

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
        elif line != 'BaseModel':
            print("** class doesn't exist **")
        else:
            new = BaseModel()
            print(new.id)

    def do_show(self, line):
        """Prints the string representation of an instance based
        on the class name and id"""
        new_line = line.split()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
