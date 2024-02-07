#!/usr/bin/python3
"""
Write a class Square that inherits from Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class that inherits from Rectangle
    """

    def __init__(self, size):
        """
        Class instantiation
        """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
