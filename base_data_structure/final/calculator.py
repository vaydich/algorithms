#63714644

import operator

class Stack:
    def __init__(self, list_in_postfix_notation):
        self._stack = []
        self._operators = ['+', '-', '*', '/']
        self._list_in_postfix_notation = list_in_postfix_notation

    def pop(self):
        return self._stack.pop()

    def push(self, value):
        self._stack.append(value)

    def get_calc_result(self):
        for note in self._list_in_postfix_notation:
            if note in self._operators:
                correct_operator = self.get_correct_operator(note)
                first_operand = self.pop()
                second_operand = self.pop()
                result = (
                    getattr(operator, correct_operator)
                    (int(first_operand), int(second_operand))
                )
                self.push(result)
            else:
                self.push(note)

        return self.pop()

    def get_correct_operator(self, note):
        if note == '+':
            correct_operator = 'add'
        elif note == '-':
            correct_operator = 'sub'
        elif note == '*':
            correct_operator = 'mul'
        else:
            correct_operator = 'floordiv'

        return correct_operator


if __name__ == '__main__':
    line_in_postfix_notation = input()
    list_in_postfix_notation = line_in_postfix_notation.split()
    stack = Stack(list_in_postfix_notation)
    print(stack.get_calc_result())
