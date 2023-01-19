#!/usr/bin/python3

import json

"""Defines a base class"""


class Base():
    """Represents the base class of all other classes in project 0x0C*
       
       Attributes:
            __nb_objects (int): The number of instantiated bases
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes an instance of Base class with id
           
           Args:
               id (int): instance id
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @classmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries
           
           Args:
               list_dictionaries: a list of dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
