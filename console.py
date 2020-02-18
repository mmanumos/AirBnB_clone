#!/usr/bin/python3
""" shebang line - defines where the interpreter is located """
import cmd
import models
from models.base_model import BaseModel
""" import moduls """


class HBNBCommand(cmd.Cmd):
    """ class with methods to work into the commands line """
    prompt = "(hbnb) "
    list_class = ["BaseModel"]
    list_err = ["** class name missing **", "** class doesn't exist **",
                "** instance id missing **", "** no instance found **",
                "** attribute name missing **", "** value missing **"]
    
    def do_create(self, line):
        """ Create a new instance of BaseModel """
        my_list = list(line.split())
        if line == "":
            print(self.list_err[0])
        elif my_list[0] == "BaseModel":
            obj = BaseModel()
            print(obj.id)
            obj.save()
        else:
            print(self.list_err[1])

    def do_show(self, line):
        """ Show object by id """
        my_list = list(line.split())
        if line == "":
            print(self.list_err[0])
        elif my_list[0] not in self.list_class:
            print(self.list_err[1])
        elif len(my_list) == 1:
            print(self.list_err[2])
        else:
            my_dic = models.storage.all()
            if ("BaseModel." + my_list[1]) in my_dic.keys():
                print(my_dic["BaseModel." + my_list[1]])
            else:
                print(self.list_err[3])

    def do_destroy(self,line):
        """ delete object by id """
        my_list = list(line.split())
        if line == "":
            print(self.list_err[0])
        elif my_list[0] not in self.list_class:
            print(self.list_err[1])
        elif len(my_list) == 1:
            print(self.list_err[2])
        else:
            my_dic = models.storage.all()
            if ("BaseModel." + my_list[1]) in my_dic.keys():
                del my_dic["BaseModel." + my_list[1]]
                models.storage.save()
            else:
                print(self.list_err[3])

    def do_all(self,line):
        """ shows all objects created """
        my_list = list(line.split())
        if len(line) == 0 or my_list[0] in self.list_class:
            print(models.storage.all())
        else:
            print(self.list_err[1])

    def do_update(self,line):
        """ update an object by className and id, with attribute and value """
        my_list = list(line.split())
        my_dic = models.storage.all()
        if line == "":
            print(self.list_err[0])
        elif my_list[0] not in self.list_class:
                print(self.list_err[1])
        elif len(my_list) < 2:
                print(self.list_err[2])
        else:
            if ("BaseModel." + my_list[1]) in my_dic.keys():
                if len(my_list) < 3:
                    print(self.list_err[4])
                elif len(my_list) < 4:
                    print(self.list_err[5])
                else:
                    obj_dic = my_dic["BaseModel." + my_list[1]]
                    obj_dic[my_list[2]] = my_list[3]
                    models.storage.save()
            else:
                print(self.list_err[3])
                                   
    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, line):
        """ EOF command to exit the program """
        return True

    def emptyline(self):
        """ When the comand line is empty and it's typed """
        pass

""" Executed the loop for Promp by default """
HBNBCommand().cmdloop()
