#!/usr/bin/python3

"""DEFINES THE USER CLASS."""

from models.base_model import BaseModel


class User(BaseModel):
    
    """REPRESENT A USER.

    Attributes:
        email (str): THE EMAIL OF THE USEr.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): THE LAST NAME OF THE USER.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

