# 62653481
from typing import List, Tuple


def get_total_points(key_count, given_arr):
    total_points = 0
    calc_key_count = key_count * 2
    for time_index in range(1, 10):
        n_count = get_n_count(time_index, given_arr)
        if n_count == 0:
            continue

        if n_count <= calc_key_count:
            total_points += 1

    return total_points


def get_n_count(number, given_arr) -> int:
    counter = 0
    for sub_arr in given_arr:
        for element in sub_arr:
            if element == '.':
                continue

            if element == number:
                counter += 1

    return counter


def read_input() -> Tuple[int, List[List[int]]]:
    key_count = int(input())
    matrix = []
    for _ in range(4):
        matrix.append([x if x == '.' else int(x) for x in input().strip()])
    return key_count, matrix


if __name__ == '__main__':
    key_count, matrix = read_input()
    n_total_points = get_total_points(key_count, matrix)
    print(n_total_points)
