#!/usr/bin/python3
"""
Module containing the Base class
"""

import json


class Base:
    """
    Class Base with private attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instantiation of class which checks for id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
