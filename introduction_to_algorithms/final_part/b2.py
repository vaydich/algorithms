#62553440

from typing import List, Tuple


def n_counter(n, arr):
    counter = 0
    for sub_arr in arr:
        for k in sub_arr:
            if k == '.':
                continue

            if k == n:
                counter += 1
    return counter


def read_input() -> Tuple[int, List[List[int]]]:
    k = int(input())
    matrix = []
    for i in range(4):
        matrix.append([x if x == '.' else int(x) for x in input().strip()])
    return k, matrix


k, matrix = read_input()

n_points = 0
for t in range(1, 10):
    n_count = n_counter(t, matrix)
    if n_count == 0:
        continue

    if n_count <= k * 2:
        n_points += 1

print(n_points)