from typing import List, Tuple


def get_sum(number_list: List[int], k: int) -> List[int]:
    n = int(''.join(str(x) for x in number_list))
    sum = n + k
    return [int(i) for i in str(sum)]


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    number_list = list(map(int, input().strip().split()))
    k = int(input())
    return number_list, k


number_list, k = read_input()
# number_list, k = ([1, 2, 0, 0, ], 34)
# get_sum(number_list, k)
print(" ".join(map(str, get_sum(number_list, k))))
