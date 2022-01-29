from random import choice


def is_bigger(section1, section2):
    if section1[1] > section2[1]:
        return True
    elif section1[1] == section2[1]:
        if section1[2] < section2[2]:
            return True
        elif section1[2] == section2[2]:
            return section1[0] < section2[0]

    return False


def partition(array, pivot):
    center = [val for val in array if val == pivot]
    less = [val for val in array if not is_bigger(val, pivot) and not val == pivot]
    greater = [val for val in array if is_bigger(val, pivot) and not val == pivot]
    return less, center, greater


def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = choice(array)
        less, center, greater = partition(array, pivot)
        return quick_sort(greater) + center + quick_sort(less)


def read_input():
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
    sorted_participants = quick_sort(participants)
    for participant in sorted_participants:
        print(participant[0])
