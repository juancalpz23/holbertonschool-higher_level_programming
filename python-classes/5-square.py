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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """
    Define the square area
    """

    def area(self):
        return self.__size * self.__size
    
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            count = 1
            while(count <= self.size):
                print("#" * self.__size)
                count += 1
