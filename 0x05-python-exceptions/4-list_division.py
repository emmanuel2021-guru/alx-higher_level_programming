#!/usr/bin/python3
def list_division(my_list1, my_list2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            new_list.append(my_list1[i] / my_list2[i])
        except TypeError:
            new_list.append(0)
            print("wrong type")
        except ZeroDivisionError:
            new_list.append(0)
            print("division by 0")
        except IndexError:
            new_list.append(0)
            print("out of range")
        finally:
            if i == (list_length - 1):
                return new_list
