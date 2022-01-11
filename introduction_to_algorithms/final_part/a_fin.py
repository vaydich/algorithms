# 62652071
from typing import List


def get_distances(given_arr: List[int]) -> List[int]:
    distances = [0] * len(given_arr)
    left_zero_idx = 0
    is_first_zero = True
    init_val = 0

    for number_index, number in enumerate(given_arr):
        if number != 0:
            init_val += 1
            distances[number_index] = init_val
            continue

        init_val = 0
        if is_first_zero:
            for interval_index in range(left_zero_idx, interval_index):
                distances[interval_index] = number_index - interval_index
        else:
            for interval_index in range(left_zero_idx, number_index):
                distances[interval_index] = min(
                    abs(left_zero_idx - interval_index),
                    number_index - interval_index
                )

        left_zero_idx = number_index
        is_first_zero = False

    return distances


def read_input() -> List[int]:
    number_len = int(input())
    number_list = list(map(int, input().strip().split()))
    return number_list


if __name__ == '__main__':
    input_arr = read_input()
    distances = get_distances(input_arr)
    print(' '.join(str(distance) for distance in distances))
