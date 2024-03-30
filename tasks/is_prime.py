__all__ = ("is_prime",)


def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    if number <= 3 and number > 1:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    index_number = 5
    while index_number * index_number <= number:
        if number % index_number == 0 or number % (index_number + 2) == 0:
            return False
        index_number += 6
    return True
print(is_prime(5))
