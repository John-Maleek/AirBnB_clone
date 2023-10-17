#!/usr/bin/python3
"""
My file storage file
"""

import os

class FileStorage:
    """
    My file storage class
    """
    def __init__(self, directory):
        """init method that initialize attributes
        """
        self.directory = directory
        os.makedirs(directory, exist_ok=True)

    def save(self, instance):
        filename = os.path.join(self.directory, f"{instance.__class__.__name__}_{instance.id}.json")
        instance.save_to_file(filename)

    def load(self, cls, id):
        filename = os.path.join(self.directory, f"{cls.__name__}_{id}.json")
        if os.path.exists(filename):
            return cls.load_from_file(filename)
        return None
