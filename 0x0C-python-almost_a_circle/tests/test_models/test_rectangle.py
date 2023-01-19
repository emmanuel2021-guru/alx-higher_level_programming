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
        self.assertAlmostEqual(b.x, 0)
        self.assertAlmostEqual(b.y, 5)

        c = Rectangle(10, 2, 0, 5, 22) 
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

    def test_width_err(self):
        """Test for any errors on width"""
        d = Rectangle(5, 1, 2, 4)
        with self.assertRaises(TypeError):
            d.width = "five"
        with self.assertRaises(ValueError):
            d.width = -5
            d.width = 0

    def test_height_err(self):
        """Test for any errors on height"""
        d = Rectangle(5, 1, 2, 4)
        with self.assertRaises(TypeError):
            d.height = "one"
        with self.assertRaises(ValueError):
            d.height = -6
            d.height = 0

    def test_x_err(self):
        """Test for any errors on x"""
        d = Rectangle(5, 1, 2, 4)
        with self.assertRaises(TypeError):
            d.x = "two"
        with self.assertRaises(ValueError):
            d.x = -8

    def test_y_err(self):
        """Test for any errors on y"""
        d = Rectangle(5, 1, 2, 4)
        with self.assertRaises(TypeError):
            d.y = "four"
        with self.assertRaises(ValueError):
            d.y = -5

    def test_area(self):
        """Tests the area function"""
        r1 = Rectangle(3, 2)
        self.assertAlmostEqual(r1.area(), 6)
        r2 = Rectangle(8, 6, 0, 5, 15)
        self.assertAlmostEqual(r2.area(), 48)

    def test_display(self):
        """Tests the display function"""
        r1 = Rectangle(4, 6)
        self.assertEqual(r1.display(), print("####\n####\n####\n####\n####\n####"))
        r2 = Rectangle(3, 3)
        self.assertEqual(r2.display(), print("###\n###\n###"))

    def test_str(self):
        """Tests the str function"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(print(r1), print("[Rectangle] (12) 2/1 - 4/6"))
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(print(r2), print("[Rectangle] (1) 1/0 - 5/5"))

    def test_display_with_x_y(self):
        """Tests the display function with x and y"""
        r1 = Rectangle(2, 3, 2, 2)
        self.assertEqual(r1.display(), print("\n\n  ##\n  ##\n  ##"))
        r2 = Rectangle(3, 2, 1, 0)
        self.assertEqual(r2.display(), print(" ###\n ###"))

    def test_update(self):
        """Tests the update function"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(print(r1), print("[Rectangle] (89) 10/10 - 10/10"))
        r1.update(89, 2)
        self.assertEqual(print(r1), print("[Rectangle] (89) 10/10 - 2/10"))
        r1.update(89, 2, 3)
        self.assertEqual(print(r1), print("[Rectangle] (89) 10/10 - 2/3"))
        r1.update(89, 2, 3, 4)
        self.assertEqual(print(r1), print("[Rectangle] (89) 4/10 - 2/3"))
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(print(r1), print("[Rectangle] (89) 4/5 - 2/3"))

    def test_update_with_kwargs(self):
        """Tests the update function with kwargs"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(print(r1), print("[Rectangle] (1) 10/10 - 10/1"))
        r1.update(width=1, x=2)
        self.assertEqual(print(r1), print("[Rectangle] (1) 2/10 - 1/1"))
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(print(r1), print("[Rectangle] (89) 3/1 - 2/1"))
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(print(r1), print("[Rectangle] (89) 1/3 - 4/2"))
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(print(r1), print("[Rectangle] (89) 4/5 - 2/3"))

    def test_to_dictionary(self):
        """Tests the to_dictionary function"""
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(print(r1_dictionary), print("{'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}"))
        self.assertEqual(print(type(r1_dictionary)), print("<class 'dict'>"))
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertEqual(print(r2), print("[Rectangle] (1) 1/9 - 10/2"))
        self.assertEqual(r1 == r2, False)
