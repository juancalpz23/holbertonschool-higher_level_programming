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

        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
