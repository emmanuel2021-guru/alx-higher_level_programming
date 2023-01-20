#!/usr/bin/python3

"""Module containing a class that defines a Student"""


class Student:
    """Defines a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes an instance of Student

           Args:
                first_name: First name of Student
                last_name: Last name of Student
                age: Student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves the dictionary representation of a
           Student instance
        """
        return self.__dict__
