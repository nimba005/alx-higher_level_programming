#!/bin/bash
# Sends a json post
curl -s -X POST "$1" -H "Content-Type: application/json" -d @"$2"
