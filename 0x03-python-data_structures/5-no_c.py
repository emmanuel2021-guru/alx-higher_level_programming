#!/usr/bin/python3
def no_c(my_string):
    """A function that removes all characters
       c and C from a string"""
    temp_list = list()
    new_string = ""
    for letter in my_string:
        temp_list.append(letter)

    for item in temp_list:
        if item == 'c' or item == 'C':
            temp_list.remove(item)

    for item in temp_list:
        new_string += item

    return new_string
