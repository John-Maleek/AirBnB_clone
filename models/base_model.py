#!/usr/bin/python3
"""
My Base model.
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    My base class
    """

    def __init__(self, *args, **kwargs):
        """ constructor method that initialize the attributes
        """

        if kwargs:
            # check whether kwargs is empty or not, if it is not empty:-
            for key, value in kwargs.items():
                if key == "__class__":
                    continue   # skip the __class__ key.
                setattr(self, key, value)    # set the attrribute.

                if key in ["created_at", "updated_at"]:
                    # if key is one of the two
                    #  convert datetime to object format.
                    setattr(
                        self,
                        key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    )
        else:
            # if kwargs is empty, create the id and created_at as before.
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """Return a string representation of the BaseModel instance
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """update the updated_at attribute with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert the object's attributes to a dictionary."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
