#63714644

def calc_postfix_notation(list):
    stack = []
    operators = ['+', '-', '*', '/']

    for note in list:
        if note in operators:
            correct_operator = note if note != '/' else '//'
            first_operand = stack.pop()
            second_operand = stack.pop()
            result = eval(f'{second_operand}{correct_operator}{first_operand}')
            stack.append(result)
        else:
            stack.append(note)

    return stack.pop()


def read_input():
    line_in_postfix_notation = input()
    list_in_postfix_notation = line_in_postfix_notation.split(' ')
    print(calc_postfix_notation(list_in_postfix_notation))

read_input()