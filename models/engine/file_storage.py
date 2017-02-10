#!/usr/bin/python3
"""
This is the FileStorage class that
serializes instances to a JSON file
and deserializes JSON file to instances
"""
import json
import datetime


json.JSONEncoder.default = lambda self, obj: (obj.isoformat() if isinstance(obj, datetime.datetime) else obj.__dict__)

class FileStorage:
    def __init__(self):
        self.__file_path = "./file.json"
        self.__objects = {}
        
    def all(self):
        return self.__objects
    
    def new(self, obj):
        #self.__objects.update({str(obj.id): obj.to_json()})
        self.__objects[obj.id] = obj

    # maybe mode='a'
    def save(self):
        with open(self.__file_path, mode='w', encoding='utf-8') as myFile:
            json.dump(self.__objects, myFile)

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
                for k in b.keys():
                    self.__objects[k] = BaseModel(b[k])
        except FileNotFoundError:
            pass

    def serialize(obj):
    #    from datetime import datetime
        if isinstance(obj, datetime):
            return obj.isoformat()
        return obj
