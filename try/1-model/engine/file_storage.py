#!/usr/bin/python3
"""
The module that serializes instances to a JSON file and
deserialize JSON file to instanceis.
"""

import json
import models
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    My file storage class
    """

    def __init__(self):
        """
        constructor method that initializes attributes of the instance.
        """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """
        Method that returns dictionary containing all the serialized object.
        """
        return self.__objects

    def new(self, obj):
        """
        This method sets an object in the __objects dictionary using key
        <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        serializes the __objects dictionary to JSON file specified
        in __file_path.
        """
        serialized_obj = {}
        for key, obj in self.__objects.items():
            serialized_obj[key] = obj.to_dict()

        with open(self.__file_path, 'w') as fil:
            json.dump(serialized_obj, fil)

    def reload(self):
        """
        Deserializes the JSON file back into the __objects dictionary.
        """
        try:
            with open(self.__file_path, 'r') as fil:
                json_data = fil.read()
                if json_data:
                    data = json.load(fil)
                    for key, obj_dict in data.items():
                        class_name, obj_id = key.split('.')

                        if class_name == 'User':
                            self.__objects[key] = User(**obj_dict)
                        else:
                            self.__objects[key] = BaseModel(**obj_dict)
        except (FileNotFoundError, json.JSONDecodeError):
            pass
