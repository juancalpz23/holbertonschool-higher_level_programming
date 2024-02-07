#!/usr/bin/python3
"""
Write a Class Rectangle the inherits from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class Rectangle the inherits from BaseGeometry with
    width and height
    """

    def __init__(self, width, height):
        """
        Class instantiation
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Function that gives the area of the rectangle
        """

        return self.__width * self.__height

    def __str__(self):
        """
        Function returns the width and height of the rectangle
        """

        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
