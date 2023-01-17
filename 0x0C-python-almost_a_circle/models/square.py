#!/usr/bin/python3

from models.rectangle import Rectangle

"""Defines a Square"""


class Square(Rectangle):
    """Represents a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square instance"""
        Rectangle.__init__(self, width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        """Returns a string representation of the Square instance"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter function for the size attribute"""
        return self.width

    @size.setter
    def size(self, val):
        """Setter function for the size attribute"""
        if type(val) is int and val > 0:
            self.width = val
            self.height = val
        elif type(val) is not int:
            raise TypeError("width must be an integer")
        else:
            raise ValueError("width must be > 0")

    def update(self, *args, **kwargs):
        """Assigns argument to each attribute"""
        if len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                elif i == 1:
                    self.size = args[1]
                elif i == 2:
                    self.x = args[2]
                elif i == 3:
                    self.y = args[3]
        elif kwargs is not None:
            for key, value in kwargs.items():
                if key == "size":
                    self.size = kwargs["size"]
                elif key == "id":
                    self.id = kwargs["id"]
                elif key == "x":
                    self.x = kwargs["x"]
                elif key == "y":
                    self.y = kwargs["y"]

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""

