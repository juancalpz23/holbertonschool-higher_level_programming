#!/usr/bin/python3
"""
Write a function that writes an Object to a
text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an Object to a
    text file, using a JSON representation
    """

    with open(filename, mode="w") as my_file:
        json.dump(my_obj, my_file)
