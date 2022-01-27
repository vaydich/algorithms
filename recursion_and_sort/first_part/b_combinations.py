class EmptyInputException(Exception):
    pass


class Solution:
    DIGIT_MAP = {
        2: 'abc',
        3: 'def',
        4: 'ghi',
        5: 'jkl',
        6: 'mno',
        7: 'pqrs',
        8: 'tuv',
        9: 'wxyz',
    }

    def __init__(self):
        self.__result = []

    def gen_combinations(self, digits):
        if len(digits) == 0:
            raise EmptyInputException
        else:
            self.__solve(digits, self.__result)
            return self.__result

    def __solve(self, digits: str, result, current_str='', current_level=0):
        if current_level == len(digits):
            result.append(current_str)
            return

        for char in self.DIGIT_MAP[int(digits[current_level])]:
            self.__solve(digits, result, current_str + char, current_level + 1)


if __name__ == '__main__':
    digit_sequence = input()
    solution = Solution()
    try:
        print(' '.join(solution.gen_combinations(digit_sequence)))
    except Exception as e:
        print(e)
