#!/usr/bin/env python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.

    :param dictionary: Python dictionary to serialize
    :param filename: Output XML file name
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=False)


def deserialize_from_xml(filename):
    """
    Deserialize an XML file into a Python dictionary.

    :param filename: Input XML file name
    :return: Python dictionary
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        data = {}
        for element in root:
            data[element.tag] = element.text

        return data

    except (ET.ParseError, FileNotFoundError, OSError):
        return None
