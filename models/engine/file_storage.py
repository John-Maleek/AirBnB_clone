#!/usr/bin/python3
"""
The module that serializes instances to a JSON file and
deserialize JSON file to instanceis.
"""

import json
# from models import base_model


class FileStorage:
    """
    My file storage class
    """
    __file_path = "file.json"
    __objects = {}

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
        in __file_path
        """
        serialized_obj = {}
        for key, obj in self.__objects.items():
            try:
                serialized_obj[key] = obj.to_dict()
            except AttributeError:
                serialized_obj[key] = obj
    
        with open(self.__file_path, 'w', encoding='utf-8') as fil:
            json.dump(serialized_obj, fil)

    def reload(self):
        """
        Deserializes the JSON file back into the __objects dictionary.
        """
        try:
          with open(self.__file_path, 'r', encoding='utf-8') as fil:
                json_data = json.load(fil)
                if json_data:
                    data = json_data
                    for key, obj_dict in data.items():
                        self.__objects[key] = obj_dict
                    print(type(self.__objects))
        except (FileNotFoundError, json.JSONDecodeError):
            pass