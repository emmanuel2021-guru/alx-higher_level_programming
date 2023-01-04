#!/usr/bin/python3
"""A module that contains a function which adds 2 integers"""


def add_integer(a, b=98):
    """Adds two integers

       Args:
            a (int): first integer to be added
            b (int): second integer to be added
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
