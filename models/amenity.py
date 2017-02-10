#!/usr/bin/python3
from models.base_model import BaseModel

class Amenity(BaseModel):
    """User inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        super().__init__()
        name = ""
