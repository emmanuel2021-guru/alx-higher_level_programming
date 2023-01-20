#!/usr/bin/python3

"""Module containing function that creates an object from
   a JSON file
"""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file

       filename: the name of the JSON file to create object from
    """
    with open(filename, encoding="utf-8") as fn:
        return json.load(fn)
