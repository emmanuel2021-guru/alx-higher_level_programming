#!/bin/bash
#This script takes in a URL and displays all HTTP methods the server will accept
curl -sI "$i" | grep "Allow" | cut -d " " -f 2-
