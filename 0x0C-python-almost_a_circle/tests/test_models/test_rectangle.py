from models.rectangle import Rectangle
import unittest

"""Tests the models/rectangle.py file"""


class TestRectangle(unittest.TestCase):
    """Tests all methods in rectangle.py"""
    def test_init(self):
        """Tests the init function"""
        a = Rectangle(10, 2)
        self.assertAlmostEqual(a.width, 10)
        self.assertAlmostEqual(a.height, 2)

        b = Rectangle(10, 2, 0, 5)
        self.assertAlmostEqual(b.width, 10)
        self.assertAlmostEqual(b.height, 2)
        self.assertAlmostEqual(b.x, 0)
        self.assertAlmostEqual(b.y, 5)

        c = Rectangle(10, 2, 0, 5, 22) 
        self.assertAlmostEqual(c.width, 10)
        self.assertAlmostEqual(c.height, 2)
        self.assertAlmostEqual(c.x, 0)
        self.assertAlmostEqual(c.y, 5)
        self.assertAlmostEqual(c.id, 22)

    def test_width(self):
        """Tests the width getter and setter functions"""
        d = Rectangle(5, 1)
        self.assertAlmostEqual(d.width, 5)
        d.width = 10
        self.assertAlmostEqual(d.width, 10)
        
    def test_height(self):
        """Tests the height getter and setter functions"""
        d = Rectangle(5, 1)
        self.assertAlmostEqual(d.height, 1)
        d.height = 10
        self.assertAlmostEqual(d.height, 10)

    def test_x(self):
        """Tests the x getter and setter functions"""
        d = Rectangle(5, 1, 2, 4)
        self.assertAlmostEqual(d.x, 2)
        d.x = 10
        self.assertAlmostEqual(d.x, 10)

    def test_y(self):
        """Tests the y getter and setter functions"""
        d = Rectangle(5, 1, 2, 4)
        self.assertAlmostEqual(d.y, 4)
        d.y = 10
        self.assertAlmostEqual(d.y, 10)
