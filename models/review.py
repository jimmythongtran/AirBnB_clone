#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    """User inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        super().__init__()
        place_id = ""  # TODO: it will be the Place.id
        user_id = ""  # TODO: it will be the User.id
        text = ""
