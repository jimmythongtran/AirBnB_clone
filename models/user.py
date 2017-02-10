#!/usr/bin/python3
from models.base_model import BaseModel

class User(BaseModel):
    """User inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
