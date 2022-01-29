# 64630506
from typing import List


def broken_search(array: List[int], searched_element: int) -> int:
    left, right = 0, len(array) - 1
    while left <= right:
        array_left_el = array[left]
        if array_left_el == searched_element:
            return left

        array_right_el = array[right]
        if array_right_el == searched_element:
            return right

        middle = (right + left) // 2

        array_middle_el = array[middle]
        if array_middle_el == searched_element:
            return middle

        if array_left_el < array_middle_el:
            if array_left_el < searched_element < array_middle_el:
                right = middle - 1
            else:
                left = middle + 1
            continue

        if array_middle_el < searched_element < array_right_el:
            left = middle + 1
        else:
            right = middle - 1

    return -1


def read_input():
    array_len = int(input())
    searched_element = int(input())
    return searched_element, list(map(int, input().split()))


if __name__ == '__main__':
    given_element, given_array = read_input()
    print(broken_search(given_array, given_element))
