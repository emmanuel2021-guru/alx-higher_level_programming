#!/usr/bin/python3

"""Defines a base class"""

import json


class Base():
    """Represents the base class of all other classes in project 0x0C*

       Attributes:
            __nb_objects (int): The number of instantiated bases
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes an instance of Base class with id

           Args:
               id (int): instance id
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries

           Args:
               list_dictionaries: a list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file

           Args:
                list_objs: list of instances of Base
        """
        if list_objs is None:
            with open("{}".format(cls.__name__ + ".json"),
                      "w", encoding="utf-8") as fn:
                fn.write("[]")
        else:
            ret_list = []
            for inst in list_objs:
                if inst.__class__.__name__ == "Rectangle":
                    ret_list.append({"id": inst.id, "width": inst.width,
                                     "height": inst.height,
                                     "x": inst.x, "y": inst.y})
                elif inst.__class__.__name__ == "Square":
                    ret_list.append({"id": inst.id, "size": inst.width,
                                     "x": inst.x, "y": inst.y})
            with open("{}".format(cls.__name__ + ".json"),
                      "w", encoding="utf-8") as fn:
                fn.write(cls.to_json_string(ret_list))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation

           Args:
                jsons_string: string representing
                              a list of dictionaries
        """
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set

           Args:
                **dictionary: double pointer to a dictionary
        """
        dummy_inst = cls(1, 2, 5, 8)
        dummy_inst.update(**dictionary)
        return dummy_inst
