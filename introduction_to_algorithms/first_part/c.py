from typing import List, Tuple


def moving_average(arr: List[int], w_size: int) -> List[float]:
    result = []
    current_sum = sum(arr[0:w_size])
    result.append(current_sum/w_size)
    for i in range(0, len(arr) - w_size):
        current_sum -= arr[i]
        current_sum += arr[i + w_size]
        current_avg = current_sum/w_size
        result.append(current_avg)
    return result


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    w_size = int(input())
    return arr, w_size


print(' '.join(map(str, moving_average(*read_input()))))
