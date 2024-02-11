#!/usr/bin/python3
"""Defines a class FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances."""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    
    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        type(self).__objects[obj.__class__.__name__ + '.' + str(obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        serialized = {}
        for key, value in type(self).__objects.items():
            serialized[key] = value.to_dict()
        with open(type(self).__file_path, mode='w', encoding="UTF-8") as f:
            for key in serialized.keys():
                json.dump(serialized, f)
                f.write("\n")

    def classes(self):
        """Returns a dictionary of valid classes and their references."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        classes = {'BaseModel': BaseModel,
                    'User': User,
                    'State': State,
                    'City': City,
                    'Amenity': Amenity,
                    'Place': Place,
                    'Review': Review}
        return classes

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(type(self).__file_path, mode='r', encoding="UTF-8") as f:
                for line in f:
                    data = json.loads(line)
                    from models.base_model import BaseModel
                    from models.user import User
                    from models.state import State
                    from models.city import City
                    from models.amenity import Amenity
                    from models.place import Place
                    from models.review import Review
                    classes = {'BaseModel': BaseModel,
                               'User': User,
                               'State': State,
                               'City': City,
                               'Amenity': Amenity,
                               'Place': Place,
                               'Review': Review}
                    for key, value in data.items():
                        class_name, obj_id = key.split('.')
                        obj = classes[class_name](**value)
                        type(self).__objects[key] = obj

        except FileNotFoundError:
            pass
