#!/bin/bash
# Display the size
curl -s "$1" | wc -c
