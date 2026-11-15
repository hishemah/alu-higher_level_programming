#!/usr/bin/python3
"""Module that defines text_indentation, which splits a text on . ? :"""


def text_indentation(text):
    """Print text with 2 new lines after each of these characters: . ? :

    No printed line starts or ends with a space.

    Args:
        text (str): the text to print.

    Raises:
        TypeError: if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for delimiter in ".?:":
        text = (delimiter + "\n\n").join(
            part.strip(" ") for part in text.split(delimiter))
    print("\n".join(line.strip(" ") for line in text.split("\n")), end="")
