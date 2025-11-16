#!/usr/bin/python3
def remove_char_at(str, n):
    """
    Creates a copy of the string, removing the character at position n.
    
    Args:
        str: The input string
        n: The position (0-indexed) of the character to remove
    
    Returns:
        A new string with the character at position n removed
    """
    if n < 0 or n >= len(str):
        return str
    
    new_str = ""
    for i in range(len(str)):
        if i != n:
            new_str += str[i]
    
    return new_str
