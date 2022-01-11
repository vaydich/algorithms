from typing import List


def checker(n, idx, arr):
    if n == 0:
        return 0

    fwd_dist = None
    for i in range(idx + 1, len(arr)):
        if arr[i] != 0:
            continue
        fwd_dist = i - idx
        break

    bwd_dist = None
    for i in range(idx - 1, -1, -1):
        if arr[i] != 0:
            continue
        bwd_dist = idx - i
        break

    if bwd_dist and fwd_dist:
        return min(bwd_dist, fwd_dist)
    else:
        return bwd_dist or fwd_dist


def read_input() -> List[int]:
    n = int(input())
    number_list = list(map(int, input().strip().split()))
    return number_list


nearest_arr = []
given_arr = read_input()
for idx, n in enumerate(given_arr):
    nearest_arr.append(checker(n, idx, given_arr))

print(' '.join(str(x) for x in nearest_arr))
