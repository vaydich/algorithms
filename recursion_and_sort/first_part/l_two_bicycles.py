def binary_search(arr, value, left, right):
    # print(left, right)
    if right == left:
        if arr[left - 1] >= value:
            return left + 1 if left == 0 else left
        elif arr[right - 1] >= value:
            return right
        else:
            return -1

    mid = (left + right) // 2
    # print('mid', mid)
    if arr[mid] >= value and arr[mid - 1] >= value:
        return binary_search(arr, value, left, mid)
    else:
        return binary_search(arr, value, mid + 1, right)


if __name__ == '__main__':
    days_count = int(input())
    accumulation_list = list(map(int, input().strip().split()))
    price = int(input())

    # days_count = 6
    # accumulation_list = [1, 2, 4, 4, 6, 8]
    # price = 3

    # days_count = 6
    # accumulation_list = [1, 2, 4, 4, 4, 4]
    # price = 3

    # days_count = 6
    # accumulation_list = [1, 2, 4, 4, 4, 4]
    # price = 10

    # days_count = 6
    # accumulation_list = [1, 2, 4, 4, 4, 4]
    # price = 1

    # days_count = 6
    # accumulation_list = [1, 1, 4, 4, 4, 4]
    # price = 1

    # days_count = 7
    # accumulation_list = [1, 1, 4, 4, 4, 4, 8]
    # price = 4

    first_day = binary_search(accumulation_list, price, 0, len(accumulation_list))
    # print(' - - - - ')
    second_day = binary_search(accumulation_list, price * 2, 0, len(accumulation_list))
    # print(' - - - - ')

    print(first_day, second_day)
