#!/usr/bin/python3
"""
This is the FileStorage class that
serializes instances to a JSON file
and deserializes JSON file to instances
"""
import json
import datetime

# TODO: manage correctly serialization and deserialization of User
json.JSONEncoder.default = lambda self, obj: (obj.isoformat() if isinstance(obj, datetime.datetime) else obj.__dict__)


class FileStorage:
    def __init__(self):
        self.__file_path = "./file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[obj.id] = obj

    def save(self):
        with open(self.__file_path, mode='w', encoding='utf-8') as myFile:
            jsondict = self.__objects
            for k, v in jsondict.items():
                jsondict[k].__dict__.update({'__class__': jsondict[k].__class__.__name__})
            json.dump(jsondict, myFile)

    def reload(self):
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as myFile:
                a = myFile.read()
                b = json.loads(a)
                for key, value in b.items():
                        for k, v in value.items():
                            if k == "created_at" or k == "updated_at":
                                b[key][k] = datetime.datetime.strptime(b[key][k], '%Y-%m-%dT%H:%M:%S.%f')
                from ..base_model import BaseModel
                from ..amenity import Amenity
                from ..user import User
                from ..state import State
                from ..place import Place
                from ..review import Review
                for k, v in b.items():
                    if v['__class__'] == "BaseModel":
                        self.__objects[k] = BaseModel(b[k])
                    elif v['__class__'] == "User":
                        self.__objects[k] = User(b[k]) 
                    elif v['__class__'] == "State":
                        self.__objects[k] = State(b[k]) 
                    elif v['__class__'] == "Place":
                        self.__objects[k] = Place(b[k]) 
                    elif v['__class__'] == "Amenity":
                        self.__objects[k] = Amenity(b[k])
                    elif v['__class__'] == "Review":
                        self.__objects[k] = Review(b[k]) 
        except FileNotFoundError:
            pass

    def serialize(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return obj
