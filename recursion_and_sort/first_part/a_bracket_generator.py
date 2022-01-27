def print_brackets(sequence_length: int, sequence_str: str):
    if 10 >= sequence_length > 0:
        gen_bracket_sequences(sequence_length, sequence_str, 0, 0)


def gen_bracket_sequences(sequence_length, sequence_str, open, close):
    if len(sequence_str) == sequence_length*2:
        print(sequence_str)
    else:
        if open < sequence_length:
            gen_bracket_sequences(sequence_length, sequence_str + '(', open + 1, close)

        if close < open:
            gen_bracket_sequences(sequence_length, sequence_str + ')', open, close + 1)


if __name__ == '__main__':
    bracket_sequence_length = int(input())
    print_brackets(bracket_sequence_length, '')
