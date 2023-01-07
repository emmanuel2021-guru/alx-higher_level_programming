#!/usr/bin/python3

"""A module that prints a text with 2 new lines after
   each of these characters; . ? :
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these
       characters; . ? :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for c in text:
        if c == "." or c == "?" or c == ":":
            print(c, end="")
            print("\n\n")
        else:
            print(c, end="")
