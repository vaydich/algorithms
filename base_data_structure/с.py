# Comment it before submitting
# class Node:
#     def __init__(self, value, next_item=None):
#         self.value = value
#         self.next_item = next_item


def get_node_by_index(node, index):
    while index:
        node = node.next_item
        index -= 1

    return node


def solution(node, idx):
    if idx == 0:
        return node.next_item

    previous_node = get_node_by_index(node, idx - 1)
    next_node = get_node_by_index(node, idx + 1)
    previous_node.next_item = next_node
    return node


# def print_nodes(node) -> None:
#     while node:
#         print(node.value, end='\n')
#         node = node.next_item


# def test():
#     node3 = Node("node3", None)
#     node2 = Node("node2", node3)
#     node1 = Node("node1", node2)
#     node0 = Node("node0", node1)
#     new_head = solution(node0, 1)
#     print_nodes(new_head)


# test()