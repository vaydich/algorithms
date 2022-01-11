def get_zero_arr(given_arr):
    zero_arr = []
    for idx, x in enumerate(given_arr):
        if x != 0:
            continue
        zero_arr.append(idx)
    return zero_arr


def checker(x, idx):
    if x == 0:
        return 0

    min_delta = abs(idx - zero_idxs_arr[0])
    if len(zero_idxs_arr) > 1:
        for zidx in zero_idxs_arr:
            tmp_delta = abs(idx - zidx)
            if tmp_delta < min_delta:
                min_delta = tmp_delta

    return min_delta


def read_input():
    n = int(input())
    number_list = list(map(int, input().strip().split()))
    return number_list


nearest_arr = []
# given_arr = read_input()
given_arr = [98, 0, 10, 77, 0, 59, 28, 0, 94]
zero_idxs_arr = get_zero_arr(given_arr)
for idx, n in enumerate(given_arr):
    nearest_arr.append(checker(n, idx))

print(' '.join(str(x) for x in nearest_arr))