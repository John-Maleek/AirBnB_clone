#!/usr/bin/python3
"""Module defines a command interpreter"""


import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from datetime import datetime


classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
           'City': City, 'Amenity': Amenity, 'Place': Place, 'Review': Review, }
storage = FileStorage()
storage.reload()


class HBNBCommand(cmd.Cmd):
    """A simple command interpreter"""
    prompt = '(hbnb) '

    def emptyline(self):
        pass

    def help_emptyline(self):
        print("Execute nothing when an empty line  is entered")

    def do_EOF(self, line):
        return True

    def help_quit(self):
        print('Quit command to exit the program')

    do_exit = do_EOF
    do_quit = do_EOF

    def do_create(self, args):
        """
            Creates a new instance of BaseModel, saves it
            (to the JSON file) and prints the id
        """
        if not args:
            print("** class name missing **")
        elif args not in classes:
            print("** class doesn't exist **")
        else:
            new_instance = classes[args]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, args):
        """
            Prints the string representation of an instance
            based on the class name and id
        """
        if not args:
            print("** class name missing **")
        else:
            args = args.split()
            if args[0] not in classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                for key, val in storage.all().items():
                    if key.split('.')[1] == args[1]:
                        print(val)
                        return
                print("** no instance found **")

    def do_all(self, args):
        """
            Prints all string representation of all
            instances based or not on the class name.
        """
        storage_list = storage.all()
        all_list = []
        if args:
            args = args.split()
            if args[0] not in classes:
                print("** class doesn't exist **")
                return
            for key, val in storage_list.items():
                if key.split('.')[0] == args[0]:
                    all_list.append(str(storage_list[key]))
            print(all_list)
        else:
            for key, val in storage_list.items():
                all_list.append(str(storage_list[key]))
            print(all_list)

    def do_update(self, args):
        """
            Updates an instance based on the class name and
            id by adding or updating attribute
            (save the change into the JSON file)
        """
        if not args:
            print("** class name missing **")
        else:
            args = args.split()
            if args[0] not in classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                for key, val in storage.all().items():
                    if key.split('.')[1] == args[1]:
                        try:
                            val[args[2]] = args[3]
                            val['updated_at'] = datetime.now().strftime(
                                "%Y-%m-%dT%H:%M:%S.%f")
                        except TypeError:
                            setattr(storage.all()[key], args[2], args[3])
                            setattr(storage.all()[key], 'updated_at', datetime.now().strftime(
                                "%Y-%m-%dT%H:%M:%S.%f"))
                        storage.save()
                        return
                print("** no instance found **")

    def do_destroy(self, args):
        """
            Deletes an instance based on the class name
            and id (save the change into the JSON file
        """
        if not args:
            print("** class name missing **")
        else:
            args = args.split()
            if args[0] not in classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                for key, val in storage.all().items():
                    if key.split('.')[1] == args[1]:
                        del storage.all()[key]
                        storage.save()
                        return
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
