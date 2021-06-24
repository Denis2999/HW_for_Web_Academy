def from_number_to_base(number=155, n=3):
    base = ""
    while number > 0:
        base = str(number % n) + base
        number = number // n
    return base


print(from_number_to_base())
