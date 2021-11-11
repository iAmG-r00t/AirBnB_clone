#!/usr/bin/python3
"""
Airbnb Console
"""
import cmd
from models.base_model import BaseModel
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """
    The entry point for the command interpreter
    """
    prompt = '(hbnb) '

    def do_create(self, line):
        if line == '':
            print('** class name missing **')
        elif line != 'BaseModel':
            print('** class doesn\'t exist **')
        else:
            base_obj = BaseModel()
            storage.save()
            print(base_obj.id)

    def do_show(self, line):
        args = line.split()
        if line == '':
            print('** class name missing **')
        elif args[0] != 'BaseModel':
            print('** class doesn\'t exist **')
        else:
            if len(args) != 2:
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
        args = line.split()
        if line == '':
            print('** class name missing **')
        elif args[0] != 'BaseModel':
            print('** class doesn\'t exist **')
        else:
            if len(args) != 2:
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
    try:
        HBNBCommand().cmdloop()
    except KeyboardInterrupt:
        print()
            
        
