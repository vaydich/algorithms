#63714644

import operator


class EmptyStackError(Exception):
    pass


class Stack:
    def __init__(self, list_in_postfix_notation):
        self.__stack = []
        self.__list_in_postfix_notation = list_in_postfix_notation
        self.__operators_map = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.floordiv
        }

    def pop(self):
        if len(self.__stack) == 0:
            raise EmptyStackError
        return self.__stack.pop()

    def push(self, value):
        self.__stack.append(value)

    def get_calc_result(self):
        for note in self.__list_in_postfix_notation:
            if note in self.__operators_map:
                correct_method = self.get_correct_method(note)
                first_operand = self.pop()
                second_operand = self.pop()
                result = correct_method(int(first_operand), int(second_operand))
                self.push(result)
            else:
                self.push(note)

        return self.pop()

    def get_correct_method(self, note):
        return self.__operators_map[note]


if __name__ == '__main__':
    line_in_postfix_notation = input()
    list_in_postfix_notation = line_in_postfix_notation.split()
    stack = Stack(list_in_postfix_notation)
    print(stack.get_calc_result())
