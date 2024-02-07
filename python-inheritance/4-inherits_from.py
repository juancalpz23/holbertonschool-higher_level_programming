#!/usr/bin/python3
"""
Returns True if object is a class inherited
directly or indirectly from specified class
"""


def inherits_from(obj, a_class):
    """
    Function that returns True if obj is an instance
    inherited from a_class
    """

    return issubclass(type(obj), a_class) and type(obj) is not a_class
