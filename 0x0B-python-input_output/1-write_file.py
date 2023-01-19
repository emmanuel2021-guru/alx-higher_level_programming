#!/usr/bin/python3

"""Module containing a function that writes a string
   to a text file and returns the number of characters
   written
"""


def write_file(filename="", text=""):
    """Writes a string to a text file(utf-8) and
       returns the number of characters written

       Args:
            filename (str): name of the file to be written to
            text (str): string to be written
    """
    with open(filename, "w", encoding="utf-8") as fn:
        nw = fn.write(text)
        return nw
