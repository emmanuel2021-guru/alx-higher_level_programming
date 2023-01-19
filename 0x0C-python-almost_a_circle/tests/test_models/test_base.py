from models.base import Base
from models.rectangle import Rectangle
import unittest

"""Tests the models/base.py file"""


class TestBase(unittest.TestCase):
    """Tests all methods in base.py"""
    def test_init(self):
        """Test the init function"""
        a = Base()
        self.assertAlmostEqual(a.id, 1)
        b = Base(12)
        self.assertAlmostEqual(b.id, 12)
        c = Base(0)
        self.assertAlmostEqual(c.id, 0)

    def test_to_json_string(self):
        """Test the to_json_string function"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(print(json_dictionary), print('[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'))
        self.assertEqual(print(type(json_dictionary)), print("<class 'str'>"))
