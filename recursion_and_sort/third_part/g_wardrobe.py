def count_sort(array, k):
    counted_values = [0] * k

    for value in array:
        counted_values[value] += 1

    index = 0
    for value in range(k):
        for amount in range(0, counted_values[value]):
            array[index] = value
            index += 1


def quick_sort(array):
    less = []
    equal = []
    greater = []

    if len(array) < 2:
        return array

    pivot = array[0]
    for x in array:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        elif x > pivot:
            greater.append(x)

    return quick_sort(less) + equal + quick_sort(greater)


def read_input():
    n = input()
    return list(map(int, input().split()))


# array = [1, 1, 2, 0, 2]
# sorted_array = quick_sort(array)
# print(sorted_array)

array = read_input()
# count_sort(array, 3)
sorted_array = quick_sort(array)
print(*sorted_array)
