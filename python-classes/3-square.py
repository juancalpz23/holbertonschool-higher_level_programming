#!/usr/bin/python3
""""
Square class definition
"""

class Square:
    """"
    Square initialization with privite instance attribute size
    """

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    """
    Define the square area
    """

    def area(self):
        return self.__size * self.__size
