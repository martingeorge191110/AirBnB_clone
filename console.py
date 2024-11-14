#!/usr/bin/python3
"""module of creating the CMD class"""

import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """Custom command line interpreter for
    Airbnb project"""

    prompt = "(hbnb) "

    classes = {
        "BaseModel" : BaseModel
    }

    def do_EOF(self, line):
        """Handle EOF to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """pass the emptyline with doing nothing"""
        pass

    def do_create(self,args):
        """create new instance, 
        saves it (to the JSON file) and prints the id"""
        if not args:
            print("** class name missing **")
            return

        try:
            class_name = args.split()[0]

            if class_name not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return

            New_Inst = HBNBCommand.classes[class_name]()
            New_Inst.save()
            print(New_Inst.id)

        except NameError:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation 
        of an instance based on the class name and id"""
        cmd_line = args.split()

        if len(cmd_line) == 0:
            print("** class name missing **")
            return

        class_name = cmd_line[0]

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if len(cmd_line) < 2:
            print("** instance id missing **")
            return

        inst_id = cmd_line[1]
        key = f"{class_name}.{inst_id}"

        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    def do_destroy(self, args):
        """Deletes an instance based on the class
        name and id, then save the change"""
        cmd_line = args.split()

        if len(cmd_line) == 0:
            print("** class name missing **")
            return

        class_name = cmd_line[0]

        if cmd_line not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if len(cmd_line) < 2:
            print("** instance id missing **")
            return
        inst_id = cmd_line[1]
        key = f"{class_name}.{inst_id}"

        if key not in storage.all():
            print("** no instance found **")

        del storage.all()[key]
        storage.save()

    def do_all(self, args):
        """Prints all string representation of all
        instances based or not on the class name"""
        filt_cls_attr = []
        if args:
            class_name = args.split()[0]

            if class_name not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for obj in storage.all().values():
                if type(obj).__name__ == class_name:
                    filt_cls_attr.append(str(obj))
            print(filt_cls_attr)

        else:
            all_inst = [str(obj) for obj in storage.all().values()]
            print(all_inst)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
