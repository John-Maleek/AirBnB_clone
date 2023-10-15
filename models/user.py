#!/usr/bin/python3
"""
My user module
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    My user class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
