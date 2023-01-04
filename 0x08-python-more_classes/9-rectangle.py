#!/usr/bin/python3

"""Defines a Rectangle class"""


class Rectangle:
    """A class that represents a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

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
            type(self).number_of_instances += 1

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

    def area(self):
        """Returns the area of a rectangle object"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimeter of a rectangle object"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """String representation of a rectangle object"""
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            for h in range(self.__height):
                for w in range(self.__width):
                    print(self.print_symbol, end="")
                if h != (self.__height - 1):
                    print("\n", end="")
                else:
                    return ""

    def __repr__(self):
        """String representation of a rectangle object to be
           able to recreate a new instance by using eval()
        """
        return "Rectangle(" + str(self.__width) + ", " +\
            str(self.__height) + ")"

    def __del__(self):
        """Returns message when rectangle is deleted"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area == rect_2.area:
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size"""
        return Rectangle(size, size)
