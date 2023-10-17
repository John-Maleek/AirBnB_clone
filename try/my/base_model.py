#!/usr/bin/python3
"""
My Base module
"""
import json

class BaseModule:
    """
    My base class
    """
    def __init__(self):
        """ constructor method that initialize the attrinutes"""
        self.id = None
    
    def to_dict(self):
        """Convert the object's attributes to a dictionary."""
        return self.__dict__

    def from_dict(self, dictionary):
        """
        Initialize the objects attributes from a dictionary.
        """
        self.__dict__.update(dictionary)
    
    def save_to_file(self, filename):
        """Save the objects data to a file in JSON format."""
        with open(filename, 'w') as fil:
            json.dump(self.to_dict(), fil)

    @classmethod
    def load_from_file(cls, filename):
        """Load the object's data from a file and create an instance.
        """
        with open(filename, 'r') as fil:
            data = json.load(fil)
        instc = cls()
        instc.from_dict(data)
        return instc
