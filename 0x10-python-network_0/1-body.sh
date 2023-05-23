#!/bin/bash
# This script takes in an URL, sends a GET request to the URL, and displays the body of the response
re=$(curl -w "%{http_code}\n" -o /dev/null -s "$1") && [ "$re" -eq 200 ] && curl "$1"
