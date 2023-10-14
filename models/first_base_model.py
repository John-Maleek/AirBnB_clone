#!/usr/bin/python3
"""
My Base module
"""
import uuid
import json
from datetime import datetime


class BaseModule:
    """
    My base class
    """
    def __init__(self, *args, **kwargs):
        """ constructor method that initialize the attributes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return a string representation of the BaseModel instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """update the updated_at attribute with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Convert the object's attributes to a dictionary."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

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
