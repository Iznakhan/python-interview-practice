def prime_numbers(start: int, end: int) -> None:
    """
    Prints all prime numbers between 100 and 200.
    """
    for numbers in range(start, end + 1):
        for i in range(2, numbers):
            if numbers % i == 0:
                break
        else:
            print(numbers)


if __name__ == "__main__":
    prime_numbers(100, 200)
