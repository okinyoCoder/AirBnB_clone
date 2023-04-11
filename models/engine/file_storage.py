#!/bin/user/python3
"""This module convert the dictionary representation to a JSON string.
With this format, humans can read and all programming languages have
a JSON reader and writer.
"""
import json
from model import BaseModel
import os


class FileStorage:
    """Class contains methods and attribute that assist in conversion of
    dictionary to Json string and file.

    Attributes:
          file_path (strings): path to the JSON file (ex: file.json)
          objects (dict): empty but will store all objects by <class name>.id
    Methods:
          all(self): returns the dictionary __objects
          new(self, obj): sets in __objects the obj with key
                          <obj class name>.id
          save(self): serializes __objects to the JSON file
                     (path: __file_path)
          reload(self): deserializes the JSON file to __objects (
                        only if the JSON file (__file_path) exists
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Method that returns the dictionary __objects
        Returns:
             dictionary __objects
        """
        return Filestorage.__objects

    def new(self, obj):
        """Method that  sets in __objects the obj with key
        <obj class name>.id
        args:
            obj (object): only method parameter
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        Filestorage.__objects[key] = obj

    def save(self):
        """Method that serializes __objects to the JSON file"""
        json_string = json.dumps(Filestorage.__objects)
        with open("Filestorage.__file.json", "w") as f:
            json.dump(json_string, f)

    def reload(self):
        """Method that deserializes the JSON file to __objects
        only if the JSON file (__file_path) exists
        """
        if os.path.isfile(FileStorage.__file_path):
            with open（"Filestorage.__file.json", "r"）as f:
                Filestorage.__objects = json.load(f)
