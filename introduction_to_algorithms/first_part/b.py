import itertools
from typing import Tuple, List


def zipper(n: int, l1: List[int], l2: List[int]) -> List[int]:
    list2d = list(map(lambda i: [l1[i], l2[i]], range(0, n)))
    merged_list = list(itertools.chain.from_iterable(list2d))
    return merged_list


def read_input() -> Tuple[int, List[int], List[int]]:
    n = int(input())
    l1 = list(map(int, input().strip().split()))
    l2 = list(map(int, input().strip().split()))
    return n, l1, l2


n, l1, l2 = read_input()
print(' '.join(list(map(str, zipper(n, l1, l2)))))
