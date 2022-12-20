#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    len_my_list = 0
    count = 0
    for i in my_list:
        len_my_list += 1
    for index in range(x):
        try:
            if (type(my_list[index]) == int):
                print("{:d}".format(my_list[index]), end="")
                count += 1
            if count == x:
                break
        except (ValueError, TypeError):
            pass
        except IndexError:
            raise
    print("")
    return count
