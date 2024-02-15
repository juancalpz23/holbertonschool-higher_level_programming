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

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter (width, height)"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assign an argument to each attribute"""
        attr = ["id", "size", "x", "y"]
        _len = len(attr)
        if len(args) > 0:
            for i, argv in enumerate(args):
                if i < _len:
                    self.__setattr__(attr[i], argv)
        else:
            for k, v in kwargs.items():
                self.__setattr__(k, v)

    def to_dictionary(self):
        """
        Returns a dictionary
        representation of a Square
        """
        s_dict = {}
        s_dict["id"] = self.id
        s_dict["size"] = self.size
        s_dict["x"] = self.x
        s_dict["y"] = self.y
        return (s_dict)
