#!/usr/bin/python3
"""
My city module
"""
from base_model import BaseModel

class City(BaseModel):
    """
    My city class
    """
    def __init__(self, name, state):
        """
        Method that initialze the attribute
        """
        super().__init__()
        self.name = name
        self.state = state
