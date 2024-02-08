#!/usr/bin/python3
"""
Write a function that reads text file (UTF*)
and prints to stdout
"""


def read_file(filename=""):
    """
    Function that reads text file (UTF*)
    and prints to stdout
    """

    with open(filename, encoding="utf-8") as my_file:
        for line in my_file:
            print(line, end="")
