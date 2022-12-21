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
            if type(size) is not int:
                raise TypeError
            elif size < 0:
                raise ValueError
            else:
                self.__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
