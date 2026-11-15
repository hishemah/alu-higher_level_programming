#!/bin/bash
# Displays all the HTTP methods the server at the URL given as argument will accept
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
