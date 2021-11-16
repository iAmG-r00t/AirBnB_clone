#!/usr/bin/python3
"""
Airbnb Console
"""
import cmd
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.city import City
from models.state import State


class HBNBCommand(cmd.Cmd):
    """
    The entry point for the command interpreter
    """
    prompt = '(hbnb) '
    classes = ['BaseModel', 'User', 'Place', 'State',
               'City', 'Amenity', 'Review']

#   def parseline(self, line):
#       print (f'parseline({line}) =>')
#       ret = cmd.Cmd.parseline(self, line)
#       print (ret)
#       return ret

    def do_create(self, line):
        """
        Creates a new instance of a given class, saves it
        (to the JSON file) and prints the id
        """
        if line == '':
            print('** class name missing **')
        elif line not in HBNBCommand.classes:
            print('** class doesn\'t exist **')
        else:
            if line == 'BaseModel':
                obj = BaseModel()
            elif line == 'User':
                obj = User()
            elif line == 'Place':
                obj = Place()
            elif line == 'State':
                obj = State()
            elif line == 'City':
                obj = City()
            elif line == 'Amenity':
                obj = Amenity()
            elif line == 'Review':
                obj = Review()
            storage.save()
            print(obj.id)

    def do_show(self, line):
        """
        Prints the string representation of an
        instance based on the class name and id.
        """
        args = line.split()
        if line == '':
            print('** class name missing **')
        elif args[0] not in HBNBCommand.classes:
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
        """
        Deletes an instance based on the class name
        and id (save the change into the JSON file)
        """
        args = line.split()
        if line == '':
            print('** class name missing **')
        elif args[0] not in HBNBCommand.classes:
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
        """
        Prints all string representation of all instances
        based or not on the class name. Ex: $ all BaseModel or $ all
        """
        args = line.split()
        result = []
        if len(args) != 0:
            if args[0] not in HBNBCommand.classes:
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
        """
        Updates an instance based on the class name and
        id by adding or updating attribute
        (save the change into the JSON file). Ex: $ update
        BaseModel 1234-1234-1234 email "aibnb@mail.com".
        update <class name> <id> <attribute name> "<attribute value>"
        """
        args = line.split()
        if line == '':
            print('** class name missing **')
        elif args[0] not in HBNBCommand.classes:
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

    def do_User(self, line):
        result = []
        parse_line = cmd.Cmd.parseline(self, line)
        if parse_line[2] != ".all()":
            return cmd.Cmd.default(self, line)
        else:
            for key, value in storage.all().items():
                if type(value).__name__ == 'User':
                    result.append(value.__str__())
            print(result)

    
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
