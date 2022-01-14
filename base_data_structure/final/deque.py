#63574448

class CustomError(Exception):
    pass


class FullQueueError(CustomError):
    pass


class EmptyQueueError(CustomError):
    pass


class Deque:
    def __init__(self, max_deque_size):
        self._helper_list = [None] * max_deque_size
        self._max_deque_size = max_deque_size
        self._head = 0
        self._tail = 0

    def is_full(self) -> bool:
        return (
                (self._head == 0 and self._tail == self._max_deque_size - 1)
                or self._head == self._tail + 1
        )

    def is_empty(self) -> bool:
        return self._head == -1

    def push_front(self, x):
        if self.is_full():
            raise FullQueueError

        if self.is_empty():
            self._head = 0
            self._tail = 0
        elif self._head == 0:
            self._head = self._max_deque_size - 1
        else:
            self._head = self._head - 1

        self._helper_list[self._head] = x

    def push_back(self, x):
        if self.is_full():
            raise FullQueueError

        if self.is_empty():
            self._head = 0
            self._tail = 0
        elif self._tail == self._max_deque_size - 1:
            self._tail = 0
        else:
            self._tail = self._tail + 1

        self._helper_list[self._tail] = x

    def pop_front(self):
        if self.is_empty():
            raise EmptyQueueError

        pop_value = self._helper_list[self._head]
        self._helper_list[self._head] = None

        if self._head == self._tail:
            self._head = -1
            self._tail = -1

        else:
            if self._head == self._max_deque_size - 1:
                self._head = 0

            else:
                self._head = self._head + 1

        return pop_value

    def pop_back(self):
        if self.is_empty():
            raise EmptyQueueError

        pop_value = self._helper_list[self._tail]
        self._helper_list[self._tail] = None

        if self._head == self._tail:
            self._head = -1
            self._tail = -1

        elif self._tail == 0:
            self._tail = self._max_deque_size - 1
        else:
            self._tail = self._tail - 1

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
                getattr(deq, cmd[0])()
            except Exception:
                print('error')
        else:
            try:
                getattr(deq, cmd[0])(int(cmd[1]))
            except Exception:
                print('error')
