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

    def width(self):
        """
        Width getter
        """
        return self.__width
    
    def width(self, value):
        """
        Width setter
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        
        def height(self):
            """
            Height getter
            """
            return self.__height
        
        def height(self, value):
            """
            Height setter
            """
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
