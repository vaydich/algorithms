def to_binary(number: int) -> str:
    if number == 0:
        return '0'

    bit = []
    while number:
        bit.append(str(number % 2))
        number >>= 1

    return ''.join(bit[::-1])


def read_input() -> int:
    return int(input().strip())


print(to_binary(read_input()))
