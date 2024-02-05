#!/usr/bin/python3
"""
Define class rectangle
"""


class Rectangle:
    """
    Define rectangle with width and height
    """

    def __init__(self, width=0, height=0):
        """
        Instantiation
        """
        self.width = width
        self.height = height

    @property
    def area(self):
        """
        Area getter
        """
        return (self.width * self.height)
    
    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return ((self.width + self.height) * 2)

    @property
    def width(self):
        """
        Width getter
        """
        return self.__width
    
    @width.setter
    def width(self, value):
        """
        Width setter
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        
    @property
    def height(self):
        """
        Height getter
        """
        return self.__height
        
    @height.setter
    def height(self, value):
        """
        Height setter
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
