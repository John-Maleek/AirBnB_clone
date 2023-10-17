#!/usr/bin/python3
"""
My place module
"""
from base_model import BaseModel

class Place(BaseModel):
    """
    My place class
    """
    def __init__(self, name, city):
        """
        Method that initialze the attribute
        """
        super().__init__()
        self.name = name
        self.city = city
