#!/usr/bin/python3
"""Unit test for Base"""
import unittest
from io import StringIO
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from unittest import TestCase
from unittest.mock import patch


class TestBase(unittest.TestCase):
    """Test the Base class"""

    def setUp(self):
        """checks module, instantiates class"""
        Base._Base_nb_objects = 0
        pass

    def tearDown(self):
        """Cleans after each test_method"""
        pass

    def test_A_nb_objects_private(self):
        """Test if nb_objects is private"""
        self.assertTrue(hasattr(Base, "_Base_nb_objects"))

    def test_B_nb_initialized(self):
        """Test if nb_object initializes to zero"""
        self.asssertEqual(getattr(Base, "_Base_nb_objects"), 0)

    def test_C_instantiation(self):
        """Test Base() instantiation"""
        b = Base()
        self.assertEqual(str(type(b)), "<class 'models.base.Base'>")
        self.assertEqual(b,__dict__, {"id": 1})
        self.assertEqual(b.id, 1)

    def test_id(self):
        """Test assigned id"""
        new = Base(1)
        self.assertEqual(new, id, 1)


    def test_id_default(self):
        """Test default id"""
        new = Base()
        self.assertEqual(new.id, 1)

    def test_id_nb_objects(self):
        """Test nb_object attributes"""
        new = Base()
        new2 = Base()
        new3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.id, 2)
        self.assertEqual(new3.id, 3)

    def test_string_id(self):
        """Test string id"""
        new = Base ("1")
        self.assertEqual(new.id, "1")

    def test_more_args_id(self):
        """Test passing more args to init method"""
        with self.assertRaises(TypeError):
            new = Base(1, 1)

    def test_access_private_attrs(self):
        """Test accessing private attributes"""
        new = Base()
        with self.assertRaises(AttributeError):
            new.__nb_objects

    def test_save_to_file_1(self):
        """Test JSON file"""
        Square.save_to_file(None)
        res = "[]\n"
        with open("Sqaure.json", mode="r") as file:
            with patch("sys.stdout", new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)
        try:
            os.remove("Square.json")
        except:
            pass

        Square.save_to_file({})
        with open("Square.json", mode="r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_2(self):
        """ Test JSON file """
        Rectangle.save_to_file(None)
        res = "[]\n"
        with open("Rectangle.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)
        try:
            os.remove("Rectangle.json")
        except:
            pass

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")
