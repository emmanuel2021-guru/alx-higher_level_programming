#!/usr/bin/python3

"""This script takes in a letter and sends a POST request to
'http://0.0.0.0:5000/search_user' with the letter as a parameter"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        p_data = {'q': ""}
    else:
        p_data = {'q': sys.argv[1]}
    req = requests.post('http://0.0.0.0:5000/search_user', data=p_data)
    try:
        json_r = req.json()
        if json_r == "":
            print("No result")
        else:
            print("[{}] {}".format(json_r['id'], json_r['name']))
    except requests.exceptions.RequestException:
        print("Not a valid JSON")
