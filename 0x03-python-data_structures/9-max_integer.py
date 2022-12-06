#!/usr/bin/python3
def max_integer(my_list=[]):
    max_int = 0
    if len(my_list) == 0:
        return None
    else:
        for i in range(len(my_list)):
            if i > max_int:
                max_int = my_list[i]
        return max_int
