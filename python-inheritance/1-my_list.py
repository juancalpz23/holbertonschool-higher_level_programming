#!/usr/bin/python3
"""
Class that inherits from list
"""


class MyList():
    """
    Public instance method that prints the list, but sorted (ascending sort)
    """

    def print_sorted(self):
        print(sorted(self))