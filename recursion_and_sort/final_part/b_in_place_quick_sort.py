# 64635450
from typing import List


def quick_sort(arr: List[any], left: int, right: int):
    if left < right:
        partition_pos = partition(arr, left, right)
        quick_sort(arr, left, partition_pos - 1)
        quick_sort(arr, partition_pos + 1, right)


def partition(arr: List[any], left: int, right: int) -> int:
    left_index = left
    right_index = right - 1
    pivot = arr[right]

    while left_index < right_index:
        while left_index < right and (not is_bigger(arr[left_index], pivot)):
            left_index += 1
        while right_index > left and (is_bigger(arr[right_index], pivot) or arr[right_index] == pivot):
            right_index -= 1

        if left_index < right_index:
            arr[left_index], arr[right_index] = arr[right_index], arr[left_index]

    if is_bigger(arr[left_index], pivot):
        arr[left_index], arr[right] = arr[right], arr[left_index]

    return left_index


def is_bigger(section1: List[any], section2: List[any]) -> bool:
    if section1[1] > section2[1]:
        return True
    elif section1[1] == section2[1]:
        if section1[2] < section2[2]:
            return True
        elif section1[2] == section2[2]:
            return section1[0] < section2[0]

    return False


def read_input() -> List[any]:
    participants_amount = int(input())
    participants = []

    while participants_amount:
        participant = input()
        splitted_participant = participant.split()
        participants.append([splitted_participant[0], int(splitted_participant[1]), int(splitted_participant[2])])
        participants_amount -= 1

    return participants


if __name__ == '__main__':
    participants = read_input()
    quick_sort(participants, 0, len(participants) - 1)
    for participant in reversed(participants):
        print(participant[0])
