from typing import List, Tuple, Optional


def naive_two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                return arr[i], arr[j]

    return None


def two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    arr.sort()
    left_pointer = 0
    right_pointer = len(arr) - 1
    while left_pointer < right_pointer:
        sum = arr[left_pointer] + arr[right_pointer]
        if sum == target_sum:
            return arr[left_pointer], arr[right_pointer]

        if sum > target_sum:
            right_pointer -= 1
        else:
            left_pointer += 1

    return None


def twosum_extra_ds(numbers, X):
    previous = set()

    for A in numbers:
        Y = X - A
        if Y in previous:
            return A, Y
        else:
            previous.add(A)

    return None, None


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    target_n = int(input())
    return arr, target_n


def print_result(result: Optional[Tuple[int, int]]) -> None:
    if result is None:
        print(None)
    else:
        print(" ".join(map(str, result)))


# arr, target_sum = read_input()
arr, target_sum = ([-9, -7, -6, -1, -1, 3], 2)
print_result(two_sum(arr, target_sum))