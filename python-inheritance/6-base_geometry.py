#!/usr/bin/python3
"""
Class BaseGeometry with a public instance
that raises an Exception
"""


class BaseGeometry():
    """
    Class BaseGeometry has a public instance
    """

    def area(self):
        """
        Function that raises an Exception
        """

        raise Exception("area() is not implemented")
