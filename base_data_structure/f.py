class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        items_length = len(self.items)

        if items_length == 0:
            print('error')
            return

        return self.items.pop()

    def get_max(self):
        items_length = len(self.items)

        if items_length == 0:
            print('None')
            return

        max = self.items[0]
        for idx in range(1, items_length):
            if self.items[idx] > max:
                max = self.items[idx]

        print(max)

def read_input():
    stack = Stack()
    n = int(input())
    # cmds = [['get_max'], ['push', 7], ['pop'], ['push', -2], ['push', -1], ['pop'], ['get_max'], ['get_max']]
    # cmds = [['get_max'], ['push', 7], ['pop'], ['get_max']]
    cmds = []

    while n:
        cmd = input()
        splitted_cmd = cmd.split()
        cmds.append(splitted_cmd)
        n -= 1

    for cmd in cmds:
        if len(cmd) == 1:
            getattr(stack, cmd[0])()
        else:
            getattr(stack, cmd[0])(int(cmd[1]))

read_input()