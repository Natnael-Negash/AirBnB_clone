#!/usr/bin/python3

"""DEFINES THE CITY CLASS."""

from models.base_model import BaseModel


class City(BaseModel):
    
    """REPRESENT A CITY.

    ATTRIBUTES:
        state_id (str): THE STATE ID.
        name (str): THE NAME OF THE CITY.
    """

    state_id = ""
    name = ""

