#!/usr/bin/python3
"""
Write a function that creates an 
Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    Function that creates an 
    Object from a “JSON file”
    """

    with open(filename, mode="r") as my_file:
        my_obj = json.load(my_file)
        return (my_obj)
