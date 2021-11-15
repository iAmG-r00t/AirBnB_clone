#!/usr/bin/python3
"""
Airbnb Console
"""
import cmd
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from datetime import datetime
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    The entry point for the command interpreter
    """
    prompt = '(hbnb) '
    
    def do_create(self, line):
        classes = ['BaseModel', 'User', 'Place', 'State',
                   'City', 'Amenity', 'Review']
        if line == '':
            print('** class name missing **')
        elif line not in classes:
            print('** class doesn\'t exist **')
        else:
            if line == 'BaseModel':
                obj = BaseModel()
            elif line == 'User':
                obj = User()
            storage.save()
            print(obj.id)

    def do_show(self, line):
        classes = ['BaseModel', 'User', 'Place', 'State',
                   'City', 'Amenity', 'Review']

        args = line.split()
        if line == '':
            print('** class name missing **')
        elif args[0] not in classes:
            print('** class doesn\'t exist **')
        else:
            if len(args) < 2:
                print('** instance id missing **')
            else:
                classname = args[0]
                objid = args[1]
                key = classname + '.' + objid
                try:
                    print(storage.all()[key])
                except KeyError:
                    print('** no instance found **')

    def do_destroy(self, line):
        classes = ['BaseModel', 'User', 'Place', 'State',
                   'City', 'Amenity', 'Review']
        args = line.split()
        if line == '':
            print('** class name missing **')
        elif args[0] not in classes:
            print('** class doesn\'t exist **')
        else:
            if len(args) < 2:
                print('** instance id missing **')
            else:
                classname = args[0]
                objid = args[1]
                key = classname + '.' + objid
                try:
                    del storage.all()[key]
                    storage.save()
                except KeyError:
                    print('** no instance found **')

    def do_all(self, line):
        classes = ['BaseModel', 'User', 'Place', 'State',
                   'City', 'Amenity', 'Review']
        args = line.split()
        result = []
        if len(args) != 0:
            if args[0] not in classes:
                print('** class doesn\'t exist **')
                return
            else:
                for key, value in storage.all().items():
                    if type(value).__name__ == args[0]:
                        result.append(value.__str__())
        else:
            for key, value in storage.all().items():
                result.append(value.__str__())
        print(result)

    def do_update(self, line):
        classes = ['BaseModel', 'User', 'Place', 'State',
                   'City', 'Amenity', 'Review']
        args = line.split()
        if line == '':
            print('** class name missing **')
        elif args[0] not in classes:
            print('** class doesn\'t exist **')
        elif len(args) < 2:
            print('** instance id missing **')

        elif len(args) < 3:
            print('** attribute name missing **')
        elif len(args) < 4:
            print('** value missing **')
        else:
            classname = args[0]
            objid = args[1]
            attr = args[2]
            value = args[3]
            oob = ['id', 'created_at', 'updated_at']
            if attr in oob:
                print('** attribute can\'t be updated **')
                return
            """
            string validity test begins (incomplete)
            """
            if value[0] == '"' and value[-1] == '"' or value[0] == "'":
                if value[0] != '"':
                    print("** A string argument must be between \
double quotes **")
                    return
                value = value[1:-1]
            else:
                try:
                    for c in value:
                        if c == '.':
                            value = float(value)
                            break
                    else:
                        value = int(value)
                except ValueError:
                    print("** A string argument must \
be between double quote **")
            if (attr[0] == '"' and attr[-1] == '"')\
               or attr[0] == "'" or attr[-1] == "'":
                if attr[0] != '"' or attr[-1] == "'":
                    print("** A string argument must be between \
double quotes **")
                    return
                attr = attr[1:-1]
            """ string validity test ends """
            key = classname + '.' + objid
            try:
                instance = storage.all()[key]
                instance.__dict__[attr] = value
                instance.save()
            except KeyError:
                print('** no instance found **')

    def do_quit(self, line):
        """Quit command to exit from cmd"""
        return True

    def do_EOF(self, line):
        """Ctrl D - to kill the program or exit from cmd"""
        print()
        return True

    def emptyline(self):
        """Empty line + Enter shouldn't execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

