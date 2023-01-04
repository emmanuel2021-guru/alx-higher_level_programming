#!/usr/bin/python3

"""Defines a Rectangle class"""


class Rectangle:
    """A class that represents a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes a rectangle

           Args:
                width (int): the width of the rectangle
                height (int): the height of the rectangle
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @property
    def width(self):
        """Returns the value of width"""
        return self.__width

    @width.setter
    def width(self, val):
        """Sets the value of width

           Args:
                val (int): the value to set
        """
        if type(val) is not int:
            raise TypeError("width must be an integer")
        elif val < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = val

    @property
    def height(self):
        """Returns the value of height"""
        return self.__height

    @height.setter
    def height(self, val):
        """Sets the value of height

           Args:
                val (int): the value to set
        """
        if type(val) is not int:
            raise TypeError("height must be an integer")
        elif val < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = val
