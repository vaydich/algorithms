from typing import List


# def bubble_sort(arr_length: int, arr: List[int]):
#     for i in range(arr_length - 1):
#         for j in range(0, arr_length - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     print(*arr)


def bubble_sort(arr_length, nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(arr_length - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

        if swapped:
            print(*nums)


def read_input():
    arr_length = int(input())
    arr = [int(str_int) for str_int in input().split()]
    return arr_length, arr


if __name__ == '__main__':
    arr_length, arr = read_input()
    bubble_sort(arr_length, arr)
