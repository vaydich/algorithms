open_bracket_list = ['{', '[', '(']
close_bracket_list = ['}', ']', ')']


def is_correct_bracket_seq(bracket_list):
    stack = []

    for bracket in bracket_list:
        if bracket in open_bracket_list:
            stack.append(bracket)
        elif bracket in close_bracket_list:
            pos = close_bracket_list.index(bracket)
            if len(stack) > 0 and open_bracket_list[pos] == stack[-1]:
                stack.pop()
            else:
                return False

    return len(stack) == 0



def read_input():
    given_bracket_list = list(input())
    # given_bracket_list = ['{', '[', '(', ')', ']', '}']
    # given_bracket_list = ['{', '[', '(', ')', ']', '}']
    # given_bracket_list = ['(', '(', '[', ')', ']', '{', '}']
    # given_bracket_list = ['(', '(', '(']
    # given_bracket_list = ['(', ')']
    print(is_correct_bracket_seq(given_bracket_list))


read_input()
