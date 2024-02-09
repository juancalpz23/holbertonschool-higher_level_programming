#!/usr/bin/python3
"""
Function that returns a list of lists of
integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    FUnction to create a pascal's triangle
    """
    if n <= 0:
        return ([])
    if n == 1:
        return [[1]]
    pascal = [[1]]
    for i in range(n - 1):
        pascal.append([x + n for x, n in zip(pascal[-1] + [0],
                                             [0] + pascal[-1])])
    return pascal
