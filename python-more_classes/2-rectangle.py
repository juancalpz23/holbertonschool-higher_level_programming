#!/usr/bin/python3
"""
Class Rectangle that defines a rectangle
"""


class Rectangle:
    """
    Define a Rectangle with withd and height
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter the value of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter the value of height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Return to the rectangle area
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Return to rectangle perimeter
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)
