def check_parity(a: int, b: int, c: int) -> bool:
    n1_c = odd_or_even(a)
    n2_c = odd_or_even(b)

    if n1_c == n2_c:
        n3_c = odd_or_even(c)
        return n2_c == n3_c

    return False


def odd_or_even(n: int) -> str:
    if n % 2 == 0:
        return 'even'
    return 'odd'


def print_result(result: bool) -> None:
    if result:
        print("WIN")
    else:
        print("FAIL")


a, b, c = map(int, input().strip().split())
print_result(check_parity(a, b, c))
