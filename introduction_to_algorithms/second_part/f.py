import re


def is_palindrome(line: str) -> bool:
    patched_str = line.lower().replace(' ', '')
    matched_str = re.sub('[^a-z0-]', '', patched_str)
    reversed_str = matched_str[::-1]
    return matched_str == reversed_str


print(is_palindrome(input().strip()))
# print(is_palindrome('A man, a plan, a canal: Panama'.strip()))
# print(is_palindrome('zo'.strip()))
