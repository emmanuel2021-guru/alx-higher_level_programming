#!/bin/bash
#This script takes in a URL and displays all HTTP methods the server will accept
curl -sIL "$1" | grep "Allow:" | cut -b 8-
