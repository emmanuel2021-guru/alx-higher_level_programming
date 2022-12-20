#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError as ve:
        print(f"Exception: {ve}")
        return False
    else:
        return True
