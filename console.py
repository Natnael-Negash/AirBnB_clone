#!/usr/bin/python3

"""DEFINES THE HBNB CONSOLE."""

import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):

    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)

    if curly_braces is None:
        if brackets is None:

            return [a.strip(",") for a in split(arg)]
        
        else:

            lexer = split(arg[:brackets.span()[0]])
            retl = [a.strip(",") for a in lexer]
            retl.append(brackets.group())
            return retl
    else:

        lexer = split(arg[:curly_braces.span()[0]])
        retl = [a.strip(",") for a in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):

    """DEFINES THE HOLBERTONBNB COMMAND INTERPRETER.

    ATTRIBUTES:
        PROMPT (STR): THE COMMAND PROMPT.
    """

    prompt = '(hbnb) '

    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):

        """DO NOTHING UPON RECEIVING AN EMPTY LINE."""

        pass

    def default(self, arg):

        """DEFAULT BEHAVIOR FOR CMD MODULE WHEN INPUT IS INVALID"""

        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)

        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):

        """QUIT COMMAND TO EXIT THE PROGRAM."""
        
        return True

    def do_EOF(self, arg):

        """EOF SIGNAL TO EXIT THE PROGRAM."""

        print()
        return True

    def do_create(self, arg):
        """USAGE: CREATE <CLASS>
        CREATE A NEW CLASS INSTANCE AND PRINT ITS ID.
        """
        argl = parse(arg)

        if len(argl) == 0:
            print("** class name missing **")

        elif argl[0] not in HBNBCommand.__classes:

            print("** class doesn't exist **")

        else:
            print(eval(argl[0])().id)
            storage.save()

    def do_show(self, arg):

        """USAGE: SHOW <CLASS> <ID> OR <CLASS>.SHOW(<ID>)
        DISPLAY THE STRING REPRESENTATION OF A CLASS INSTANCE OF A GIVEN ID.
        """
        argl = parse(arg)
        objdict = storage.all()

        if len(argl) == 0:

            print("** class name missing **")

        elif argl[0] not in HBNBCommand.__classes:

            print("** class doesn't exist **")

        elif len(argl) == 1:

            print("** instance id missing **")

        elif "{}.{}".format(argl[0], argl[1]) not in objdict:

            print("** no instance found **")

        else:

            print(objdict["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):

        """USAGE: DESTROY <CLASS> <ID> OR <CLASS>.DESTROY(<ID>)
        DELETE A CLASS INSTANCE OF A GIVEN ID."""

        argl = parse(arg)
        objdict = storage.all()

        if len(argl) == 0:

            print("** class name missing **")

        elif argl[0] not in HBNBCommand.__classes:

            print("** class doesn't exist **")

        elif len(argl) == 1:

            print("** instance id missing **")

        elif "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(argl[0], argl[1])]
            storage.save()

    def do_all(self, arg):

        """USAGE: ALL OR ALL <CLASS> OR <CLASS>.ALL()
        DISPLAY STRING REPRESENTATIONS OF ALL INSTANCES OF A GIVEN CLASS.
        IF NO CLASS IS SPECIFIED, DISPLAYS ALL INSTANTIATED OBJECTS."""

        argl = parse(arg)

        if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:

            print("** class doesn't exist **")

        else:
            objl = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_count(self, arg):

        """USAGE: COUNT <CLASS> OR <CLASS>.COUNT()
        RETRIEVE THE NUMBER OF INSTANCES OF A GIVEN CLASS."""
        
        argl = parse(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):

        """USAGE: UPDATE <CLASS> <ID> <ATTRIBUTE_NAME> <ATTRIBUTE_VALUE> OR
       <CLASS>.UPDATE(<ID>, <ATTRIBUTE_NAME>, <ATTRIBUTE_VALUE>) OR
       <CLASS>.UPDATE(<ID>, <DICTIONARY>)
        UPDATE A CLASS INSTANCE OF A GIVEN ID BY ADDING OR UPDATING
        A GIVEN ATTRIBUTE KEY/VALUE PAIR OR DICTIONARY."""
        
        argl = parse(arg)
        objdict = storage.all()

        if len(argl) == 0:

            print("** class name missing **")
            return False
        
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        
        if len(argl) == 1:

            print("** instance id missing **")
            return False
        
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argl) == 4:

            obj = objdict["{}.{}".format(argl[0], argl[1])]

            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])

            else:

                obj.__dict__[argl[2]] = argl[3]

        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for l, v in eval(argl[2]).items():
                if (l in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[l]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[l])
                    obj.__dict__[l] = valtype(v)
                else:
                    obj.__dict__[l] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()

