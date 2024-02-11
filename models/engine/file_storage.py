#!/usr/bin/python3

"""DEFINES THE FILESTORAGE CLASS."""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """REPRESENT AN ABSTRACTED STORAGE ENGINE.

    Attributes:
        __file_path (str): THE NAME OF THE FILE TO SAVE OBJECTS TO.
        __objects (dict): A DICTIONARY OF INSTANTIATED OBJECTS.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):

        """RETURN THE DICTIONARY __OBJECTS."""

        return FileStorage.__objects

    def new(self, obj):

        """SET IN __OBJECTS OBJ WITH KEY <OBJ_CLASS_NAME>.ID"""

        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """SERIALIZE __OBJECTS TO THE JSON FILE __FILE_PATH."""

        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):

        """DESERIALIZE THE JSON FILE __FILE_PATH TO __OBJECTS, IF IT EXISTS."""

        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for m in objdict.values():
                    cls_name = m["__class__"]
                    del m["__class__"]
                    self.new(eval(cls_name)(**m))
        except FileNotFoundError:
            return

