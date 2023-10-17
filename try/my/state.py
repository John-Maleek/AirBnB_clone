#!/usr/bin/python3
"""
My state module
"""
from base_model import BaseModel

class State(BaseModel):
    """
    My state class
    """
    def __init__(self, name, capital_city):
        """
        Method that initialze the attribute
        """
        super().__init__()
        self.name = name
        self.capital_city = capital_city
