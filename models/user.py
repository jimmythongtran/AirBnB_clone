#!/usr/bin/python3

#TODO: NameError: name 'BaseModel is not defined'
class User(BaseModel):
    """User inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        email = ""
        password = ""
        first_name = ""
        last_name = ""
