def count_sort(array, k):
    counted_values = [0] * k

    for value in array:
        counted_values[value] += 1

    index = 0
    for value in range(k):
        for amount in range(0, counted_values[value]):
            array[index] = value
            index += 1


def read_input():
    n = int(input())
    return list(map(int, input().split()))


array = read_input()
# count_sort(array, 3)
print(*sorted(array))
# print(*array)
