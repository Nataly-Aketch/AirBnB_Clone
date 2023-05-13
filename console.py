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
from models import storage


class HBNBCommand(cmd.Cmd):
    """command processor"""
    prompt = '(hbnb) '
    cls_list = ['BaseModel', 'State', 'City', 'User',
                'Place', 'Amenity', 'Review']

    def do_EOF(self, line):
        """End of File to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        exit()

    def do_create(self, line):
        """Creates a new instance of a class, saves it (to the JSON file)
        and prints the id"""
        if not line:
            print("** class name missing **")
        elif line not in self.cls_list:
            print("** class doesn't exist **")
        else:
            new = globals()[line]()
            print(new.id)
            new.save()

    def do_show(self, line):
        """Prints the string representation of an instance based
        on the class name and id"""
        new_line = line.split()
        new_inst = BaseModel()
        if not new_line[0]:
            print("** class name missing **")
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
        """Prints all string representation of all instances
        based or not in the class name"""
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
        """Updates an instance based on the class name and
        id by adding or updating attribute"""
        input = line.split()
        if len(input) > 4:
            cls = "class name"
            attr = "attribute name"
            print("update <{}> <id> <{}> \"<attribute value>\""
                  .format(cls, attr))
        else:
            if len(input) == 0:
                print("** class name missing **")
            elif input[0] not in self.cls_list:
                print("** class doesn't exist **")
            elif len(input) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(input[0], input[1])
                if key not in storage.all():
                    print("** no instance found **")
                elif len(input) < 3:
                    print("** attribute name missing **")
                elif len(input) < 4:
                    print("** value missing **")
                else:
                    non_updatable_attributes = ["id", "created_at",
                                                "updated_at"]
                    if hasattr(storage.all()[key], input[2]) \
                            and input[2] not in non_updatable_attributes:
                        cast = type(getattr(storage.all()[key], input[2]))
                        value = cast(input[3])
                        print(type(value))
                        setattr(storage.all()[key], input[2], value)
                        storage.save()
                    elif input[2] not in non_updatable_attributes:
                        setattr(storage.all()[key], input[2],
                                input[3].strip('"').strip("'")
                                .replace("'", '"'))
                        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
