# def is_subsequence(str1: str, str2: str, str1_len: int, str2_len: int) -> bool:
#     if str1_len == 0:
#         return True
#
#     if str2_len == 0:
#         return False
#
#     if str1[str1_len - 1] == str2[str2_len - 1]:
#         return is_subsequence(str1, str2, str1_len - 1, str2_len - 1)
#
#     return is_subsequence(str1, str2, str1_len, str2_len - 1)


def is_subsequence(str1, str2):
    m = len(str1)
    n = len(str2)

    j = 0
    i = 0

    while j < m and i < n:
        if str1[j] == str2[i]:
            j = j + 1
        i = i + 1

    return j == m


def read_input():
    return input(), input()


if __name__ == '__main__':
    str1, str2 = read_input()
    print(is_subsequence(str1, str2))