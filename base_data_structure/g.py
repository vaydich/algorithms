class StackMaxEffective:
    def __init__(self):
        self.items = []
        self.max_items = []

    def push(self, item):
        items_length = len(self.items)

        if not items_length:
            self.max_items.append(item)
        else:
            if item >= self.max_items[-1]:
                self.max_items.append(item)

        self.items.append(item)

    def pop(self):
        items_length = len(self.items)

        if items_length == 0:
            print('error')
            return

        pop_item = self.items.pop()
        if pop_item == self.max_items[-1]:
            self.max_items.pop()
        return pop_item

    def get_max(self):
        items_length = len(self.items)

        if items_length == 0:
            print('None')
            return

        print(self.max_items[-1])

def read_input():
    stack = StackMaxEffective()
    n = int(input())
    # cmds = [['pop'], ['pop'], ['push', 4], ['push', -5], ['push', 7], ['pop'], ['pop'], ['get_max'], ['pop'], ['get_max']]
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