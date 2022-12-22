#!/usr/bin/python3

"""Define a square"""


class Square:
    """ Represents a square """
    def __init__(self, size=0, position=(0, 0)):
        """ Initializes a square instance
            and checks for exceptions

            Args:
                size (int): the size of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ Getter method for getting the position
            of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Setter method for setting the position
            of the square
        """
        try:
            if value[0] < 0 or value[1] < 0:
                raise TypeError
            else:
                self.__position = value
        except TypeError:
            print("position must be a tuple of 2 positive integers")

    def area(self):
        """ Returns the area of a square """
        return self.__size ** 2

    def my_print(self):
        """ Prints in stdout the square
            with the character #
        """
        if self.__size == 0:
            print("")
        else:
            if self.position[1] > 0:
                print("" * self.position[1])
            for i in range(self.__size):
                print(" " * self.position[0], end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")
