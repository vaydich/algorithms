#64113151

class FullQueueError(Exception):
    pass


class EmptyQueueError(Exception):
    pass


class Deque:
    def __init__(self, max_deque_size):
        self.__helper_list = [None] * max_deque_size
        self.__max_deque_size = max_deque_size
        self.__head = -1
        self.__tail = 0

    def is_full(self) -> bool:
        return (
                (self.__head == 0 and self.__tail == self.__max_deque_size - 1)
                or self.__head == self.__tail + 1
        )

    def is_empty(self) -> bool:
        return self.__head == -1

    def push_front(self, value):
        if self.is_full():
            raise FullQueueError

        if self.is_empty():
            self.__head = 0
            self.__tail = 0
        elif self.__head == 0:
            self.__head = self.__max_deque_size - 1
        else:
            self.__head = self.__head - 1

        self.__helper_list[self.__head] = value

    def push_back(self, value):
        if self.is_full():
            raise FullQueueError

        if self.is_empty():
            self.__head = 0
            self.__tail = 0
        elif self.__tail == self.__max_deque_size - 1:
            self.__tail = 0
        else:
            self.__tail = self.__tail + 1

        self.__helper_list[self.__tail] = value

    def pop_front(self):
        if self.is_empty():
            raise EmptyQueueError

        pop_value = self.__helper_list[self.__head]
        self.__helper_list[self.__head] = None

        if self.__head == self.__tail:
            self.__head = -1
            self.__tail = -1

        else:
            if self.__head == self.__max_deque_size - 1:
                self.__head = 0

            else:
                self.__head = self.__head + 1

        return pop_value

    def pop_back(self):
        if self.is_empty():
            raise EmptyQueueError

        pop_value = self.__helper_list[self.__tail]
        self.__helper_list[self.__tail] = None

        if self.__head == self.__tail:
            self.__head = -1
            self.__tail = -1

        elif self.__tail == 0:
            self.__tail = self.__max_deque_size - 1
        else:
            self.__tail = self.__tail - 1

        return pop_value


if __name__ == '__main__':
    n_cmds = int(input())
    deq_max_size = int(input())
    deq = Deque(deq_max_size)
    cmds = []

    while n_cmds:
        cmd = input()
        splitted_cmd = cmd.split()
        cmds.append(splitted_cmd)
        n_cmds -= 1

    for cmd in cmds:
        if len(cmd) == 1:
            try:
                print(getattr(deq, cmd[0])())
            except Exception:
                print('error')
        else:
            try:
                getattr(deq, cmd[0])(int(cmd[1]))
            except Exception:
                print('error')
