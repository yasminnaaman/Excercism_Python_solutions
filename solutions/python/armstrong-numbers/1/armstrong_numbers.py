def is_armstrong_number(number):
    if not isinstance(number, int):
        raise TypeError("number must be an integer")
    if number < 0:
        raise ValueError("number must be non-negative")

    digits = str(number)
    power = len(digits)
    total = sum(int(digit)**power for digit in digits)

    return total == number
