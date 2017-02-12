#!/usr/bin/python3
from models.base_model import BaseModel


class Place(BaseModel):
    """User inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            super().__init__(args[0], kwargs)
        else:
            super().__init__()
        city_id = ""  # TODO: it will be the City.id
        user_id = ""  # TODO: it will be the User.id
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenities = [""]   # TODO: it will be the list of Amenity.id
