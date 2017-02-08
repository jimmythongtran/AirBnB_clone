#!/usr/bin/python3
"""
This is the FileStorage class that
serializes instances to a JSON file
and deserializes JSON file to instances
"""
import json


class FileStorage:
    def __init__(self):
        self.__file_path = "./file.json"
        self.__objects = {}
        
    def all(self):
        return self.__objects
    
    def new(self, obj):
        self.__objects.update({str(obj.id): obj.to_json()})
        
    # maybe mode='a'
    def save(self):
        with open(self.__file_path, mode='w', encoding='utf-8') as myFile:
            json.dump(self.__objects, myFile)

    def reload(self):
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as myFile:
                json.load(self.__objects, myFile)
        except FileNotFoundError:
            pass
