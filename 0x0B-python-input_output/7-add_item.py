#!/usr/bin/python3

"""Module containing a script that adds all arguments to
   a python list, and save them to a file
"""

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
import sys

arg_list = list()
try:
    for item in load_from_json_file("add_item.json"):
        arg_list.append(item)
except FileNotFoundError:
    f = open("add_item.json", "w", encoding="utf-8")
    f.close()
for i in range(len(sys.argv)):
    if i > 0:
        arg_list.append(sys.argv[i])
save_to_json_file(arg_list, "add_item.json")
