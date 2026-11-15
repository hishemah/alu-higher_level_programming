#!/bin/bash
# Sends a GET request to the URL given as argument and displays the body of a 200 status code response
curl -sfL "$1"
