#!/usr/bin/python3

"""Module containing a function that returns an object
   (Python data structure) represented by a JSON string
"""
import json


def from_json_string(my_str):
    """Returns an object (Python data structure) represented
       by a JSON string

       Args:
            my_str: JSON string to be decoded
    """
    return json.loads(my_str)
