def prime_numbers(start: int, end: int) -> None:
    """
    Prints all prime numbers between a given range.

    Args:
        start (int): The starting number.
        end (int): The ending number.
    """
    for number in range(start, end + 1):
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            print(number)


if __name__ == "__main__":
    prime_numbers(100, 200)
