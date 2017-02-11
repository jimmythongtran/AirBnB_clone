#!/usr/bin/python3
"""
This file contains the BaseModel defining all
common attributes/methods for other classes
"""
import uuid
import datetime
import json
from . import storage


class BaseModel:
    """
    This is the class for BaseModel
    """
    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            self.__dict__ = args[0]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_json(self):
        self.__dict__.update({'__class__': "BaseModel"})
        return self.__dict__
