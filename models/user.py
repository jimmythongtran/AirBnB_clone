#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """User inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            super().__init__(args[0], kwargs)
        else:
            super().__init__()
        email = ""
        password = ""
        first_name = ""
        last_name = ""
