def merge_sort(array):
    if len(array) == 1:
        return array

    mid = len(array) // 2
    left = merge_sort([array[i] for i in range(mid)])
    right = merge_sort([array[i] for i in range(mid, len(array))])
    result = [[]] * len(array)

    l, r, k = 0, 0, 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result[k] = left[l]
            l += 1
        else:
            result[k] = right[r]
            r += 1
        k += 1

    while l < len(left):
        result[k] = left[l]
        l += 1
        k += 1

    while r < len(right):
        result[k] = right[r]
        r += 1
        k += 1

    return result


def check_sections(sections_arr):
    if len(sections_arr) == 1:
        return sections_arr

    result = []
    i, j = 0, 1
    while i < len(sections_arr) - 1 and j < len(sections_arr):
        if sections_arr[i][0] <= sections_arr[j][0] <= sections_arr[i][1]:
            if sections_arr[j][1] > sections_arr[i][1]:
                sections_arr[i][1] = sections_arr[j][1]
            if j == len(sections_arr) - 1:
                result.append(sections_arr[i])
            j += 1
        else:
            result.append(sections_arr[i])
            if j == len(sections_arr) - 1:
                result.append(sections_arr[j])
            i += 1
            j += 1

    return result


def read_input():
    n = int(input())
    result = []
    for i in range(n):
        result.append(list(map(int, input().strip().split())))
    return result


sections_arr = read_input()
# sections_arr = [[7, 8], [7, 8], [2, 3], [6, 10]]
# sections_arr = [[2, 3], [5, 6], [3, 4], [3, 4]]
# sections_arr = [[1, 3], [3, 5], [4, 6], [5, 6], [2, 4], [7, 10]]
#
# print(' - - - ', merge_sort(sections_arr))

# sort_by_comparator(sections_arr, is_first_section_weaker)
# print(sections_arr)
union_sections = check_sections(sorted(sections_arr))
for section in union_sections:
    print(*section)
