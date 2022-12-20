#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    len_my_list = 0
    for item in my_list:
        len_my_list += 1
    try:
        for i in range(len_my_list):
            print("{}".format(my_list[i]), end="")
            count += 1
            if count == x:
                break
        print("")
        return count
    except IndexError:
        return count
