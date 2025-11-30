# task_03_xml.py

import xml.etree.Element Tree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into an XML file.

    Parameters:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the file to save the XML data.
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserializes an XML file into a Python dictionary.

    Parameters:
        filename (str): The name of the XML file to read.

    Returns:
        dict: A dictionary with string keys and string values.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}
    for child in root:
        result[child.tag] = child.text
    return result
