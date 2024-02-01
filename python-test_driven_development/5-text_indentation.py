#!/usr/bin/python3
"""
Prints text
"""


def text_indentation(text):
    """
    Function prints a text with 2 new lines
    after each of these characters: ., ? and :
    """

    if isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    txt_len = len(text)
    while i < txt_len:
        if text[i] in ('.', '?', ':'):
            print("{}\n".format(text[i]))
            while i + 1 < txt_len and text[i + 1] == " ":
                i += 1
        else:
            print(text[1], end='')
        i += 1
