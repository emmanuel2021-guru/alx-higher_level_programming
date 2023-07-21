#!/usr/bin/python3

"""This script takes in a letter and sends a POST request to 
'http://0.0.0.0:5000/search_user' with the letter as a parameter"""

import requests
import sys


if __name__ == "__main__":
    if sys.argv[1] == None:
        p_data = {'q': ""}
    else:
        p_data = {'q': sys.argv[1]}
    req = requests.post('http://0.0.0.0:5000/search_user', data=p_data)
    try:
        if req.json() == "":
            print("No result")
        else:
            print(req.json())
    except JSONDecodeError:
        print("Not a valid JSON")
