def reverse_string(text: str) -> str:
    """
    Reverse a string.

    Args:
        text (str): The string to reverse.

    Returns:
        str: The reversed string.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string.")

    reverse_str = ""

    for char in text:
        reverse_str = char + reverse_str

    return reverse_str


result = reverse_string("Python")
print(result)
