class Queue:
    def __init__(self, n):
        self._queue = []
        self._max_n = n

    def is_empty(self):
        return len(self._queue) == 0

    def size(self):
        print(len(self._queue))

    def push(self, x):
        if len(self._queue) == self._max_n:
            print('error')
            return

        self._queue.append(x)

    def pop(self):
        if self.is_empty():
            print('None')
            return

        print(self._queue[0])
        del self._queue[0]

    def peek(self):
        if self.is_empty():
            print('None')
            return

        print(self._queue[0])


def read_input():
    n_cmd = int(input())
    n = int(input())
    queue = Queue(n)
    # queue = Queue(1)
    # n = int(input())
    # cmds = [['peek'], ['push', 5], ['push', 2], ['peek'], ['size'], ['size'], ['push', 1], ['size']]
    # cmds = [['push', 1], ['size'], ['push', 3], ['size'], ['push', 1], ['pop'], ['push', 1], ['pop'],  ['push', 3], ['push', 3]]
    cmds = []

    while n_cmd:
        cmd = input()
        splitted_cmd = cmd.split()
        cmds.append(splitted_cmd)
        n_cmd -= 1

    for cmd in cmds:
        if len(cmd) == 1:
            getattr(queue, cmd[0])()
        else:
            getattr(queue, cmd[0])(int(cmd[1]))

    # print(queue._queue)

read_input()