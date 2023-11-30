#!/bin/bash
# Send a request to a url
curl -sI -w '%{response_code}' "$1" -o /dev/null
