#!/bin/bash
# Bash script that sends a JSON POST request to an URL and displays the body of the response.
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"
