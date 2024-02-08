#!/usr/bin/python3
"""
Write a function that writes a string to a text file
(UTF8) and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    Function that writes a string to a text file
    (UTF8) and returns the number of characters added
    """

    with open(filename, mode="+a", encoding="utf-8") as my_file:
        contents = my_file.write(text)
    return contents
