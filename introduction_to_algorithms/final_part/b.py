k = 3
# input_arr = [[1, 0, 1, 7], [9, 0, 0, 9], [1, 2, 1, 1], [9, 9, 1, 0]]
input_arr = [[1, 2, 3, 1], [2, 0, 0, 2], [2, 0, 0, 2], [2, 0, 0, 2]]
# input_arr = [[1, 1, 1, 1], [9, 9, 9, 9], [1, 1, 1, 1], [9, 9, 1, 1]]
# input_arr = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]


def n_counter(n):
    counter = 0
    for sub_arr in input_arr:
        for k in sub_arr:
            if k != n:
                continue
            counter += 1
    return counter


n_points = 0
for t in range(1, 10):
    n_count = n_counter(t)
    if n_count == 0:
        continue

    if n_count <= k * 2:
        n_points += 1

print(n_points)
