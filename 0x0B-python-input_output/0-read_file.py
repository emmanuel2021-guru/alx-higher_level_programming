#!/usr/bin/python3

"""Module containing a function that reads a text file
   and prints it to stdout
"""

def read_file(filename=""):
    """Reads a text file(utf-8) and prints it to stdout

       Args:
            filename: the name of the file to be read
    """
    with open(filename, encoding="utf-8") as fn:
        for line in fn:
            print(line, end="")
