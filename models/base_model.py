#!/usr/bin/python3
"""
This file contains the BaseModel defining all
common attributes/methods for other classes
"""
import uuid
import datetime
import json


class BaseModel:
    """
    This is the class for BaseModel
    """
    def __init__(self):
        self.id = uuid.uuid4()
        self.created_at = datetime.datetime.now()

    def __str__(self):
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_json(self):
        return json.dumps(self)
