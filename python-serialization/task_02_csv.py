#!/usr/bin/python3
"""Module to convert a CSV file to JSON format."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to JSON format and save it to 'data.json'.

    Args:
        csv_filename (str): The CSV file to read.

    Returns:
        bool: True if conversion was successful, False if an exception occurs.
    """
    try:
        with open(csv_filename, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data_list = [row for row in reader]

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data_list, json_file)

        return True
    except (OSError, csv.Error, json.JSONDecodeError):
        return False
