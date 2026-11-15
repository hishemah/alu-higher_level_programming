#!/bin/bash
# Sends a JSON POST request with the contents of the file given as second argument and displays the body of the response
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
