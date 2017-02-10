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
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        # check this
        if isinstance(args, dict):
            self.__dict__ = args
        else:
            storage.new(self)
          #  self.id = str(uuid.uuid4())
          #  self.created_at = datetime.datetime.now()

    def __str__(self):
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now()
       # check this
       storage.save()

    def to_json(self):
        self.__dict__.update({'__class__': "BaseModel"})
        return self.__dict__
