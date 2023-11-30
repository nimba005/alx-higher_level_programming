#!/bin/bash
# Take url
curl -Is "$1" | grep "Allow:" | cut -d ' ' -f 2-
