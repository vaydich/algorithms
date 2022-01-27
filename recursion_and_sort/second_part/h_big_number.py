def is_first_concat_bigger(num1, num2):
    return int(f'{num1}{num2}') > int(f'{num2}{num1}')


def sort(array, bigger):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and bigger(item_to_insert, array[j - 1]):
            array[j] = array[j - 1]
            j -= 1
        array[j] = item_to_insert


def read_input():
    arr_length = int(input())
    arr = [int(str_int) for str_int in input().split()]
    return arr_length, arr


if __name__ == '__main__':
    arr_length, arr = read_input()
    sort(arr, is_first_concat_bigger)
    print(''.join([str(n) for n in arr]))
