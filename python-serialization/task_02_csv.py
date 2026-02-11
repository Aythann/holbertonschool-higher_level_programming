#!/usr/bin/env python3
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to JSON format and save it to data.json

    :param csv_filename: CSV file to read
    :return: True if successful, False otherwise
    """
    try:
        data = []

        with open(csv_filename, newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data.append(row)

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file)

        return True

    except (FileNotFoundError, OSError):
        return False
