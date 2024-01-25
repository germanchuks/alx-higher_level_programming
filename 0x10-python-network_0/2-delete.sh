#!/bin/bash
# Bash script that sends a DELETE request to passed as the first argument, and displays the body of the response.
curl -sX DELETE "$1"
