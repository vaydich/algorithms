def bubble(a):
    n = len(a)
    count = 0
    for i in range(n-1):
        changed = False
        for j in range(0, n-i-1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                changed = True
                count += 1
        if changed:
            print(*a)

    if not count:
        print(*a)


def read_input():
    arr_length = int(input())
    arr = [int(str_int) for str_int in input().split()]
    return arr_length, arr


if __name__ == '__main__':
    arr_length, arr = read_input()
    bubble(arr)
