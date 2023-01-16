#!/usr/bin/python3

"""Defines a class "Base"""


class Base(object):
    """Represents the base class of all other classes in project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes an instance of Base class with id"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
