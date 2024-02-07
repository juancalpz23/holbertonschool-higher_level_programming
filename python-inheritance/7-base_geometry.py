#!/usr/bin/python3
"""
Class BaseGeometry with a public instance
that raises an Exception
"""


class BaseGeometry():
    """
    Class BaseGeometry has 2 public instances
    """

    def area(self):
        """
        Function that raises an Exception
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value
        """
        
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
