#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


def max_integer(lst=[]):
    """
    Function to find and return the max integer in a list of integers

    Args:
        lst (list of int): The list of integers.

    Returns:
        int or None: The maximum integer in the list. Returns None if the list is empty.
    """
    if len(lst) == 0:
        return None
    result = lst[0]
    i = 1
    while i < len(lst):
        if lst[i] > result:
            result = lst[i]
        i += 1
    return result

class TestMaxIntegerFunction(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 5, 3, 8, 2]), 8)
        self.assertEqual(max_integer([-10, -5, -8, -2]), -2)
        self.assertIsNone(max_integer([]))

    def test_max_integer_with_non_integer_elements(self):
        with self.assertRaises(TypeError):
            max_integer(["a", "b", "c"])

if __name__ == "__main__":
    unittest.main()