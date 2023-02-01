#!/usr/bin/python3
"""Unittest for "max_integer" function
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest for "max_integer"
    """
    def test_max_integer(self):
        """Unittest for "max_integer"
        """
        self.assertAlmostEqual(max_integer([10, 5, 8, 9, 2]), 10)
        self.assertAlmostEqual(max_integer([5, 8, 10, 1, 2]), 10)
        self.assertAlmostEqual(max_integer([1, 8, 5, 3, 10]), 10)
        self.assertAlmostEqual(max_integer([1, -8, 5, 3, 10]), 10)
        self.assertAlmostEqual(max_integer([-2, -8, -5, -1, -10]), -1)
        self.assertAlmostEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([]), None)
