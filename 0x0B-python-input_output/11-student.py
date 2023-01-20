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

    def to_json(self, attrs=None):
        """Retrieves the dictionary representation of a
           Student instance

           Args:
                attrs: List of attributes
        """
        if attrs is not None:
            flag = 0
            for item in attrs:
                if type(item) is str:
                    flag = 1
                else:
                    flag = 0
                    break
            if flag == 1:
                temp_list = []
                for item in attrs:
                    try:
                        temp_list.append((item, self.__dict__[item]))
                    except KeyError:
                        continue
                return dict(temp_list)
            else:
                return self.__dict__
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance

           Args:
                json: dictionary of attributes to replace
        """
        self.__dict__ = json
