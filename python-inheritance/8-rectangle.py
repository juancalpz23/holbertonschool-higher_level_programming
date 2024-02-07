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
