#!/usr/bin/python3

"""Module containing function that returns the JSON
   representation of an object
"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object

       Args:
            my_obj: object whose JSON representation
                    is to be returned
    """
    return json.dumps(my_obj)
