#!/bin/bash
# Bash script that sends a request to an URL, and displays only the status code of the response.
curl -s -o /dev/null -w "%{http_code}" "$1"