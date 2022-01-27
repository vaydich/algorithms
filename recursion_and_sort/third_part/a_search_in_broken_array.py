def broken_search(array, element):
    left, right = 0, len(array) - 1
    while left <= right:
        array_left = array[left]
        if array_left == element:
            return left

        array_right = array[right]
        if array_right == element:
            return right

        middle = (right + left) // 2

        array_middle = array[middle]
        if array_middle == element:
            return middle

        if array_left < array_middle:
            if array_left < element < array_middle:
                right = middle
            else:
                left = middle
            continue

        if array_middle < element < array_right:
            left = middle
        else:
            right = middle

    return -1


if __name__ == '__main__':
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    # arr = [3, 6, 7]
    # arr = [5, 1]
    print(broken_search(arr, 19))