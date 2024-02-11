#!/usr/bin/python3

"""DEFINES THE REVIEW CLASS."""

from models.base_model import BaseModel


class Review(BaseModel):
    """REPRESENT A REVIEW.

    Attributes:
        place_id (str): THE PLACE ID.
        user_id (str): The User id.
        text (str): THE TEXT OF THE REVIEW.
    """

    place_id = ""
    user_id = ""
    text = ""

