from typing import List, Tuple


def get_neighbours(matrix: List[List[int]], row: int, col: int) -> List[int]:
    row_l = len(matrix)
    col_l = len(matrix[0])
    for i in range(max(0, row - 1), min(row + 2, row_l)):
        for j in range(max(0, col - 1, min(col + 2, col_l))):
            if i != row or j != col:
                print(matrix[i][j])


def read_input() -> Tuple[List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())
    return matrix, row, col


# matrix, row, col = read_input()
# print(" ".join(map(str, get_neighbours(matrix, row, col))))
matrix, row, col = ([[1, 2, 3], [0, 2, 6], [7, 4, 1], [2, 7, 0]], 1, 1)
get_neighbours(matrix, row, col)
