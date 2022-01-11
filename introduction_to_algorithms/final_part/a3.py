#62546871

def fill_distance(given_arr):
    left_zero_idx = 0
    is_first_zero = True
    init_val = 0
    for idx, x in enumerate(given_arr):
        if x != 0:
            init_val += 1
            init_arr[idx] = init_val
            continue

        init_val = 0
        if is_first_zero:
            for n in range(left_zero_idx, idx):
                init_arr[n] = idx - n
        else:
            for n in range(left_zero_idx, idx):
                init_arr[n] = min(abs(left_zero_idx - n), idx - n)

        left_zero_idx = idx
        is_first_zero = False


def read_input():
    n = int(input())
    number_list = list(map(int, input().strip().split()))
    return number_list


input_arr = read_input()
init_arr = [0 for x in range(len(input_arr))]
fill_distance(input_arr)
print(' '.join(str(x) for x in init_arr))


# import sys
#
# def main():
#     num_lines = int(input())  # Считываем первую строку из потока ввода
#     output_numbers = []
#     for i in range(num_lines):
#         line = sys.stdin.readline().rstrip()
#         value_1, value_2 = line.split()
#         value_1 = int(value_1)
#         value_2 = int(value_2)
#         result = value_1 + value_2
#         output_numbers.append(str(result))
#     print('\n'.join(output_numbers))
#
# if __name__ == '__main__':
#     main()