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
                data_dict[child.tag] = None
                continue
            text_lower = text.lower()
            # Try boolean first
            if text_lower == "true":
                data_dict[child.tag] = True
            elif text_lower == "false":
                data_dict[child.tag] = False
            else:
                # Try integer
                try:
                    data_dict[child.tag] = int(text)
                except ValueError:
                    # Try float
                    try:
                        data_dict[child.tag] = float(text)
                    except ValueError:
                        # Keep as string
                        data_dict[child.tag] = text
        return data_dict
    except (ET.ParseError, FileNotFoundError):
        return {}
