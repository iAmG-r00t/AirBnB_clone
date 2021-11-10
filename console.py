#!/usr/bin/python3
"""
Airbnb Console
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    The entry point for the command interpreter
    """
    prompt = '(hbnb) '

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
            
        
