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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation
        of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes JSON string representation
        of list_objs to a file
        """
        fn = cls.__name__ + ".json"
        list_dict = []
        if list_objs is not None:
            for i in list_objs:
                list_dict.append(cls.to_dictionary(i))
        with open(fn, mode="w") as myFile:
            myFile.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list of the JSON
        string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return[]
        return json.loads(json_string)
