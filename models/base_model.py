#!/usr/bin/python3
"""defining Basemodel."""

import models
from uuid import uuid4
from datetime import datetime


class Basemodel:
    """"representing a basemodel.

    Attributes:
        id (string): unique id which must be converted to string.
        created_at (datetime): when the instance is created.
        updated_at (datetime): will be updated everytime the object changes.
    """
    id = str(uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __init__(self, *args, **kwags):
        """building dictonary."""
        if (len(kwargs) != 0):
            for key, value in kwargs.items():
                if (key == 'id'):
                    self.id = kwargs.get(key)
                if (key == 'created_at'):
                    self.created_at = datetime.strptime(
                        kwargs.get(key), '%Y-%m-%dT%H:%M:%S.%f')
                if (key == 'updated_at'):
                    self.updated_at = datetime.strptime(
                        kwargs.get(key), '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """prints string method."""
        return ("[{self.__class__.__name__}] ({}) {}"
                .format(self.id, self.__dict__, self=self))

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary."""
        my_dict = self.__dict__.copy()
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return (my_dict)
