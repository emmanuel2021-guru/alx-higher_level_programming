#!/usr/bin/python3

"""Define a square"""


class Square:
    """ Represents a square """
    def __init__(self, size=0):
        """ Initializes a square instance
            and checks for exceptions

            Args:
                size (int): the size of the square
        """
        self.size = size

    @property
    def size(self):
        """ Getter method for getting the size
            of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter method for setting the size
            of the square

            Args:
                value (int): the size of the square
        """
        try:
            if type(value) is not int:
                raise TypeError
            elif value < 0:
                raise ValueError
            else:
                self.__size = value
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")

    def area(self):
        """ Returns the area of a square """
        return self.size ** 2
