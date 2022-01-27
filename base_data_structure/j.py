class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


class Queue:
    def __init__(self):
        self._size = 0
        self._head = None
        self._tail = None

    def put(self, x):
        node = Node(x, None)

        if self._size == 0:
            self._head = node
        else:
            tail_node = self._tail
            tail_node.next_item = node

        self._tail = node
        self._size += 1

    def get(self):
        if self._size == 0:
            print('error')
            return

        head_node = self._head
        self._head = head_node.next_item
        head_node.next_item = None
        self._size -= 1
        print(head_node.value)

    def size(self):
        print(self._size)



# def solution(node) -> None:
#     while node:
#         print(node.value, end='\n')
#         node = node.next_item


def read_input():
    linked_queue = Queue()
    n = int(input())
    # cmds = [['put', -34], ['put', -23], ['get'], ['size'], ['get'], ['size'], ['get'], ['get'], ['put', 80], ['size']]
    cmds = []

    while n:
        cmd = input()
        splitted_cmd = cmd.split()
        cmds.append(splitted_cmd)
        n -= 1

    for cmd in cmds:
        # print('cmd', cmd[0])
        if len(cmd) == 1:
            getattr(linked_queue, cmd[0])()
        else:
            getattr(linked_queue, cmd[0])(int(cmd[1]))

    # print(queue._queue)

read_input()