from models.square import Square
import unittest

"""Tests models/square.py"""


class TestSquare(unittest.TestCase):
    """Tests all methods in rectangle.py"""
    def test_init(self):
        """Tests the init function"""
        s1 = Square(5)
        self.assertAlmostEqual(s1.area(), 25)
        s2 = Square(2, 2)
        self.assertAlmostEqual(s2.area(), 4)
        s3 = Square(3, 1, 3)
        self.assertAlmostEqual(s3.area(), 9)

    def test_str(self):
        """Tests the str function"""
        s1 = Square(5)
        self.assertEqual(print(s1), print("[Square] (1) 0/0 - 5"))
        s2 = Square(2, 2)
        self.assertEqual(print(s2), print("[Square] (2) 2/0 - 2"))
        s3 = Square(3, 1, 3)
        self.assertEqual(print(s3), print("[Square] (3) 1/3 - 3"))

    def test_size(self):
        """Tests the size getter and setter functions"""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(s1.size, 10)

    def test_size_err(self):
        """Tests for any errors on size"""
        s1 = Square(5)
        with self.assertRaises(TypeError):
            s1.size = "ten"
        with self.assertRaises(ValueError):
            s1.size = 0

    def test_update(self):
        """Tests the update function"""
        s1 = Square(5)
        s1.update(10)
        self.assertEqual(print(s1), print("[Square] (10) 0/0 - 5"))
        s1.update(1, 2)
        self.assertEqual(print(s1), print("[Square] (1) 0/0 - 2"))
        s1.update(1, 2, 3)
        self.assertEqual(print(s1), print("[Square] (1) 3/0 - 2"))
        s1.update(1, 2, 3, 4)
        self.assertEqual(print(s1), print("[Square] (1) 3/4 - 2"))
        s1.update(x=12)
        self.assertEqual(print(s1), print("[Square] (1) 12/4 - 2"))
        s1.update(size=7, y=1)
        self.assertEqual(print(s1), print("[Square] (1) 12/1 - 7"))
        s1.update(size=7, id=89, y=1)
        self.assertEqual(print(s1), print("[Square] (89) 12/1 - 7"))
