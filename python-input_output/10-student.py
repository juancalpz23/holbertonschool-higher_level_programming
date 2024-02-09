#!/usr/bin/python3
"""
Write a class Student that defines a student
"""


class Student:
    """
    The attributes for the class
    """

    def __init__(self, first_name, last_name, age):
        """
        Class instantiation
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation
        of a Student instance
        """

        if attrs is None:
            return (self.__dict__)
        my_dict = {}
        for i in attrs:
            if i in self.__dict__ and type(i) is str:
                my_dict[i] = self.__dict__.get(i)
        return my_dict
