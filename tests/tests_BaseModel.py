#!/usr/bin/python3
"""
Unittest for BaseModel
"""
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(TestCase):
    def test_createModel(self):
        my_model = BaseModel()

    def test_BaseModelAssignment(self):
        my_model = BaseModel()
        my_model.aString = "a string"
        my_model.aNumber = 98

    def test_BaseModelCreatedAt(self):
        my_model = BaseModel()
        self.assertEqual(type(datetime.now()), type(my_model.created_at))

    def test_BaseModelJSON(self):
        my_model = BaseModel()
        my_jsondict = my_model.__dict__
        my_jsondict['__class__'] = my_model.__class__.__name__
        my_model_json = my_model.to_json()
        for key, value in my_model_json.items():
            self.assertEqual(my_jsondict[key], value)
        

    def test_BaseModelPrint(self):
        my_model = BaseModel()
        expected_print = "[{}] ({}) {}\n".format(my_model.__class__.__name__, my_model.id, my_model.__dict__)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(my_model) 
            self.assertEqual(fake_out.getvalue(), expected_print)
