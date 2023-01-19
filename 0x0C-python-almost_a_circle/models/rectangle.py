#!/usr/bin/python3

"""Defines a rectangle class that inherits from Base"""

from models.base import Base


class Rectangle(Base):
    """Represents a rectangle class inheriting from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle instance

           Args:
               width (int): Rectangle width
               height (int): Rectangle height
               x (int): Rectangle offset on x-axis
               y (int): Rectangle offset on y-axis
               id (int): Base id
        """
        if type(width) is int and width > 0:
            self.__width = width
        elif type(width) is not int:
            raise TypeError("width must be an integer")
        else:
            raise ValueError("width must be > 0")

        if type(height) is int and height > 0:
            self.__height = height
        elif type(height) is not int:
            raise TypeError("height must be an integer")
        else:
            raise ValueError("height must be > 0")

        if type(x) is int and x >= 0:
            self.__x = x
        elif type(x) is not int:
            raise TypeError("x must be an integer")
        else:
            raise ValueError("x must be >= 0")

        if type(y) is int and y >= 0:
            self.__y = y
        elif type(y) is not int:
            raise TypeError("y must be an intger")
        else:
            raise ValueError("y must be >= 0")

        Base.__init__(self, id)

    @property
    def width(self):
        """Sets/Gets the value of width"""
        return self.__width

    @width.setter
    def width(self, val):
        if type(val) is int and val > 0:
            self.__width = val
        elif type(val) is not int:
            raise TypeError("width must be an integer")
        else:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        """Sets/Gets the value of height"""
        return self.__height

    @height.setter
    def height(self, val):
        if type(val) is int and val > 0:
            self.__height = val
        elif type(val) is not int:
            raise TypeError("height must be an integer")
        else:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """Sets/Gets the value of x"""
        return self.__x

    @x.setter
    def x(self, val):
        if type(val) is int and val >= 0:
            self.__x = val
        elif type(val) is not int:
            raise TypeError("x must be an integer")
        else:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """Sets/Gets the value of y"""
        return self.__y

    @y.setter
    def y(self, val):
        if type(val) is int and val >= 0:
            self.__y = val
        elif type(val) is not int:
            raise TypeError("y must be an integer")
        else:
            raise ValueError("y must be >= 0")

    def area(self):
        """Returns the area value of the Rectangle instance"""
        return (self.width * self.height)

    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""
        if self.x == 0 and self.y == 0:
            for i in range(self.height):
                for j in range(self.width):
                    print("#", end="")
                print("\n", end="")
        else:
            print("\n" * self.y, end="")
            for i in range(self.height):
                print(" " * self.x, end="")
                for j in range(self.width):
                    print("#", end="")
                print("\n", end="")

    def __str__(self):
        """Returns a string representation of a Rectangle instance"""
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Updates the Rectangle

           Args:
               *args: list of arguments
                      1st argument - id attribute
                      2nd argument - width attribute
                      3rd argument - height attribute
                      4th argument - x attribute
                      5th argument - y attribute
               **kwargs: double pointer to a dictionary; key/value
        """
        if len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                elif i == 1:
                    self.width = args[1]
                elif i == 2:
                    self.height = args[2]
                elif i == 3:
                    self.x = args[3]
                elif i == 4:
                    self.y = args[4]
        elif kwargs is not None:
            for key, value in kwargs.items():
                if key == "width":
                    self.width = kwargs["width"]
                elif key == "height":
                    self.height = kwargs["height"]
                elif key == "id":
                    self.id = kwargs["id"]
                elif key == "x":
                    self.x = kwargs["x"]
                elif key == "y":
                    self.y = kwargs["y"]

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        rect_dict = {"id": self.id, "width": self.width,
                     "height": self.height, "x": self.x, "y": self.y}
        return rect_dict
