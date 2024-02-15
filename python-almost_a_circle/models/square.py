#!/usr/bin/python3
"""
Module for the Square class
that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square inherits
    from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructors from Rectangle"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of square"""
        return ("[Square] ({}) {}/{} - {}".format
                (self.id, self.x, self.y, self.width))
