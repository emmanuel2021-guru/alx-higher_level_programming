from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
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

    def test_save_to_file(self):
        """Test the save_to_file function"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(print(file.read()), print('{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}, {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]'))

    def test_from_json_string(self):
        """Test the from_json_string function"""
        list_input = [
                {'id': 89, 'width': 10, 'height': 4},
                {'id': 7, 'width': 1, 'height': 7}
                ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(print("[{}] {}".format(type(list_input), list_input)), print("[<class 'list'>] [{'height': 4, 'width': 10, 'id': 89}, {'height': 7, 'width': 1, 'id': 7}]"))
        self.assertEqual(print("[{}] {}".format(type(json_list_input), json_list_input)), print('[<class \'str\'>] [{"height": 4, "width": 10, "id": 89}, {"height": 7, "width": 1, "id": 7}]'))
        self.assertEqual(print("[{}] {}".format(type(list_output), list_output)), print("[<class 'list'>] [{'height': 4, 'width': 10, 'id': 89}, {'height': 7, 'width': 1, 'id': 7}]"))

    def test_create(self):
        """Tests the create function"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(print(r1), print("[Rectangle] (1) 1/0 - 3/5"))
        self.assertEqual(print(r2), print("[Rectangle] (1) 1/0 - 3/5"))
        self.assertEqual(print(r1 is r2), print("False"))
        self.assertEqual(print(r1 == r2), print("False"))

    def test_load_from_file(self):
        """Tests the load_from_file function"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(print("{}".format(list_rectangles_input[0])), print("[Rectangle] (1) 2/8 - 10/7"))
        self.assertEqual(print("{}".format(list_rectangles_input[1])), print("[Rectangle] (2) 0/0 - 2/4"))
        self.assertEqual(print("{}".format(list_rectangles_output[0])), print("[Rectangle] (1) 2/8 - 10/7"))
        self.assertEqual(print("{}".format(list_rectangles_output[1])), print("[Rectangle] (2) 0/0 - 2/4"))

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertEqual(print("{}".format(list_squares_input[0])), print("[Square] (5) 0/0 - 5"))
        self.assertEqual(print("{}".format(list_squares_input[1])), print("[Square] (6) 9/1 - 7"))
        self.assertEqual(print("{}".format(list_squares_output[0])), print("[Square] (5) 0/0 - 5"))
        self.assertEqual(print("{}".format(list_squares_output[1])), print("[Square] (6) 9/1 - 7"))
