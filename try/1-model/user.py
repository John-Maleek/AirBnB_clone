#!/usr/bin/python3
"""
My user module
"""
from .base_model import BaseModel


class User(BaseModel):
    """
    My user class
    """
    def __init__(self, email, password, first_name, last_name):
        """
        constructor method that initialize the attribut's.
        """
        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
