def find_largest(list1: list) -> float:
    """
    Finds the largest number from a list.

    Args:
        list1 (list): A list containing int and float values.

    Returns:
        float: The largest number.

    Raises:
        TypeError: If input is not a list.
        ValueError: If the list is empty.
        ValueError: If the list contains non-numeric elements.
        ValueError: If the list contains duplicate numbers.
    """

    # First check the type of the input.
    # We expect a list, so reject anything else with TypeError.
    if not isinstance(list1, list):
        raise TypeError("list1 must be a list.")

    # An empty list has no element from which we can find the largest number.
    if list1 == []:
        raise ValueError("List should not be empty.")

    # Check every element because the list should contain only numbers.
    # int and float are both accepted as valid numeric values.
    for elements in list1:
        if not isinstance(elements, (int, float)):
            raise ValueError("List must contain only numbers.")

    # Compare the length of the original list with the length of the set.
    # set removes duplicate values, so different lengths mean duplicates exist.
    if len(list1) != len(set(list1)):
        raise ValueError("Duplicates are not allowed.")

    # Start with the first element as the current largest number.
    largest = list1[0]

    # Compare every number with the current largest.
    # If a bigger number is found, update largest.
    for num in list1:
        if num > largest:
            largest = num

    # Return the largest value to whoever called the function.
    return largest


if __name__ == "__main__":

    # input() always gives us a string.
    # split(",") separates the user's comma-separated values.
    list1 = input("Enter Numbers by commas: ")

    # Convert each separated value from string to float.
    list1 = [float(x) for x in list1.split(",")]

    # Pass the list to the function and store the returned largest value.
    result = find_largest(list1)

    # Display the result to the user.
    print(result)
