#!/usr/bin/python3
"""
Print square function
"""


def print_square(size):
    """
    Function that prints a # square
    """

    if type(size) is not int or type(size) is float:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
