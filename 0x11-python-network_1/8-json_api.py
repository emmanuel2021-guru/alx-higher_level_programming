#!/usr/bin/python3

"""This script takes in a letter and sends a POST request to 
'http://0.0.0.0:5000/search_user' with the letter as a parameter"""

import requests
import sys


if __name__ == "__main__":
    if sys.argv[1] is None:
        p_data = {'q': ""}
    else:
        p_data = {'q': sys.argv[1]}
    req = requests.post('http://0.0.0.0:5000/search_user', data=p_data)
    try:
        json_r = req.json()
        if json_r == "":
            print("No result")
        else:
            print("{} {}".format(json_r[0]['id'], json_r[0]['name']))
    except JSONDecodeError:
        print("Not a valid JSON")
