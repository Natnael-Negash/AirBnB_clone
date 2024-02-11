#!/usr/bin/python3

"""DEFINES THE AMENITY CLASS."""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """REPRESENT AN AMENITY.

    ATTRIBUTES:
        NAME (STR): THE NAME OF THE AMENITY.
    """

    name = ""

