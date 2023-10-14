#!/usr/bin/python3
"""
My user module
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    My user class
    """

    def __init__(self, username, email):
        """
        constructor method that initialize the attribut's
        """
        super().__init__()
        self.username = username
        self.email = email
