from models.base import Base
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
        self.assertAlmostEqual(c.id, 0
