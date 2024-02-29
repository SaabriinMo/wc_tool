"""
ccwc - word, line, character, and byte count.

Author: @saabriinmo
"""

import os
import sys


def wc_byte_count(filename: str) -> int:
    """Calculate the Byte count

    Args:
        filename (string): the file path

    Returns:
        int: returns the byte count of the file
    """

    byte_count = os.stat(filename)
    return byte_count.st_size


def wc_line_count(filename: str) -> int:
    """Calculates the line count in a file

    Args:
        filename (string): the file path

    Returns:
        int: returns the line count of the file
"""

    with open(filename, 'r', encoding='utf-8') as file:
        output = len(file.readlines())
    return output


def wc_word_count(filename) -> int:
    """Calculates the word count in a file

    Args:
        filename (string): the file path

    Returns:
        int: returns the word count of the file
    """

    with open(filename, 'r', encoding='utf-8') as file:
        output = len(file.read().split())
    return output


def wc_char_count(filename) -> int:
    """Calculate the character count in a file

    Args:
        filename (string): the file path

    Returns:
        int: returns the character count of file
    """

    with open(filename, 'rb') as file:
        chars = file.read()
        char_count = len(chars.decode())

    return char_count
