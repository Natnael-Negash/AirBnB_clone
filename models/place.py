#!/usr/bin/python3

"""DEFINES THE PLACE CLASS."""

from models.base_model import BaseModel


class Place(BaseModel):

    """REPRESENT A PLACE.

    Attributes:
        city_id (str): THE CITY ID.
        user_id (str): The User id.
        name (str): The name of the place.
        description (str): THE DESCRIPTION OF THE PLACE.
        number_rooms (int): The number of rooms of the place.
        number_bathrooms (int): THE NUMBER OF BATHROOMS OF THE PLACE.
        MAX_GUEST (INT): THE MAXIMUM NUMBER OF GUESTS OF THE PLACE.
        price_by_night (int): The price by night of the place.
        latitude (float): The latitude of the place.
        longitude (float): The longitude of the place.
        amenity_ids (list): A LIST OF AMENITY IDS.
    """


    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

