#!/usr/bin/python3

"""DEFINES THE BASEMODEL CLASS."""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:

    """REPRESENTS THE BASEMODEL OF THE HBNB PROJECT."""

    def __init__(self, *args, **kwargs):
        """INITIALIZE A NEW BASEMODEL.

        Args:
            *args (any): UNUSED.
            **kwargs (dict): KEY/VALUE PAIRS OF ATTRIBUTES.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for l, v in kwargs.items():
                if l == "created_at" or l == "updated_at":
                    self.__dict__[l] = datetime.strptime(v, tform)
                else:
                    self.__dict__[l] = v
        else:
            models.storage.new(self)

    def save(self):

        """UPDATE UPDATED_AT WITH THE CURRENT DATETIME."""

        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):

        """RETURN THE DICTIONARY OF THE BASEMODEL INSTANCE.

        INCLUDES THE KEY/VALUE PAIR __CLASS__ REPRESENTING
        THE CLASS NAME OF THE OBJECT.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """RETURN THE PRINT/STR REPRESENTATION OF THE BASEMODEL INSTANCE."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)

