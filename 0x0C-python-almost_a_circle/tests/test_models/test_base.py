#!/usr/bin/python3
""" Test Base Models"""
from models.base import Base
from unittest import TestCase
from unittest.mock import patch
from models.square import Square
from models.rectangle import Rectangle
from io import StringIO
import unittest

class TestBaseMethods(unittest.TestCase):
    """ BASE CLASS TESTING """
    def setUp(self):
        """ EACH TEST METHOD TESTING"""
        Base._Base__nb_objects = 0
    def test_id(self):
        """ ID TESTING"""
        new = Base(1)
        self.assertEqual(new.id, 1)
    def test_id_default(self):
        """ NB OBJ ATTR TESTING"""
        new = Base()
        new2 = Base()
        new3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.id, 2)
        self.assertEqual(new3.id, 3)
    def test_id_mix(self):

