from typing import Tuple


def to_binary(number: int) -> str:
    if number == 0:
        return '0'

    bit = []
    while number:
        bit.append(str(number % 2))
        number >>= 1

    return ''.join(bit[::-1])


def get_sum(first_number: str, second_number: str) -> str:
    return to_binary(int(first_number, 2) + int(second_number, 2))


def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number


first_number, second_number = read_input()
# first_number, second_number = ('1', '1')
print(get_sum(first_number, second_number))
