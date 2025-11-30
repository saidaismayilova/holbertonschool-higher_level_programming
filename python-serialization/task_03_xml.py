#!/usr/bin/python3
"""Module for serializing and deserializing Python dictionaries to/from XML."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to XML and save it to a file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The filename to save the XML to.
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        # Serialize booleans as lowercase, others as strings
        if isinstance(value, bool):
            child.text = str(value).lower()
        else:
            child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize an XML file into a Python dictionary.

    Args:
        filename (str): The XML file to read.

    Returns:
        dict: The deserialized Python dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        data_dict = {}

        for child in root:
            text = child.text
            if text is None:
                data_dict[child.tag] = ""
                continue

            text_lower = text.lower()
            # Boolean check first
            if text_lower == "true":
                data_dict[child.tag] = True
            elif text_lower == "false":
                data_dict[child.tag] = False
            else:
                # Try integer or float conversion
                try:
                    if "." in text:
                        data_dict[child.tag] = float(text)
                    else:
                        data_dict[child.tag] = int(text)
                except ValueError:
                    data_dict[child.tag] = text

        return data_dict
    except (ET.ParseError, FileNotFoundError):
        return {}
