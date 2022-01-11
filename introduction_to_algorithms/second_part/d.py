from typing import List


def checker(i, arr):
    # print('--------')
    # print(i, arr[i])
    if i - 1 >= 0 and i + 1 < len(arr):
        # print(1, arr[i] > arr[i - 1] and arr[i] > arr[i + 1])
        return arr[i] > arr[i - 1] and arr[i] > arr[i + 1]

    if i - 1 < 0:
        # print(2, arr[i], arr[i + 1], arr[i] > arr[i + 1])
        return arr[i] > arr[i + 1]

    if i + 1 > len(arr) - 1:
        # print(3,  arr[i] > arr[i - 1])
        return arr[i] > arr[i - 1]

    return False


def get_weather_randomness(temperatures: List[int]) -> int:
    if len(temperatures) == 1:
        return len(temperatures)

    count = 0
    for i in range(0, len(temperatures)):
        if abs(temperatures[i]) > 273:
            continue
        if checker(i, temperatures):
            count += 1

    return count


def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures


temperatures = read_input()
# temperatures = [-1, -10, -8, 0, 2, 0, 5]
# temperatures = [1, 2, 5, 4, 8]
# temperatures = [-159, -248, 8, -23, -45, -131, -169, -184, 159, -241]
# temperatures = [-254, -234, -223, -214, -211, -211, -208, -195, -175, -175, -164, -146, -142, -126, -116, -109, -104,
#                 -93, -87, -82, 5, 8, 19, 30, 105, 108, 111, 112, 123, 130, 169, 171, 191, 200, 234, 237, 245, 251, 253, 261]
# print(len(temperatures))
print(get_weather_randomness(temperatures))
