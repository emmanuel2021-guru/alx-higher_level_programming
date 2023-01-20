#!/usr/bin/python3

"""Module containing function that writes an object to a
   text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file, using a JSON representation

       Args:
            my_obj: object to be written to file
            filename: the name of the file to be written to
    """
    with open(filename, "w", encoding="utf-8") as fn:
        json.dump(my_obj, fn)
