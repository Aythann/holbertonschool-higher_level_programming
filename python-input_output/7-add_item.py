#!/usr/bin/python3
"""
Adds all command line arguments to a Python list and saves them to a file.
"""

import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    data = load_from_json_file(filename)
except (FileNotFoundError, json.decoder.JSONDecodeError):
    data = []

data.extend(sys.argv[1:])
save_to_json_file(data, filename)
