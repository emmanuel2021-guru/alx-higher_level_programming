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
        try:
            self.__size = size
            if size < 0:
                raise ValueError
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
