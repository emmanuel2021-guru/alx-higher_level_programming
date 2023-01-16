#!/usr/bin/python3

from models.base import Base

"""Defines a rectangle class that inherits from Base"""


class Rectangle(Base):
    """Represents a rectangle class inheriting from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle instance"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        Base.__init__(self, id)

    @property
    def width(self):
        """Getter function for width"""
        return self.__width

    @width.setter
    def width(self, val):
        """Setter function for width"""
        self.__width = val

    @property
    def height(self):
        """Getter function for height"""
        return self.__height

    @height.setter
    def height(self, val):
        """Setter function for width"""
        self.__height = val

    @property
    def x(self):
        """Getter function for x"""
        return self.__x

    @x.setter
    def x(self, val):
        """Setter function for x"""
        self.__x = val

    @property
    def y(self):
        """Getter function for y"""
        return self.__y

    @y.setter
    def y(self, val):
        """Setter function for y"""
        self.__y = val
