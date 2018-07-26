import random
from Leetcode.OtherAlgorithm.ListNode import *


def delete_node(head, node):
    if node.next is None:
        p = head
        while p.next is not node:
            p = p.next
        p.next = None
        del node
    else:
        p = node.next
        node.data = p.data
        node.next = p.next
        del p


if __name__ == '__main__':
    del_node_index = random.randint(0, 10)
    del_node = None

    print('del node index', del_node_index)
    print('----------------')

    head = ListNode(None)
    for i in range(10):
        node = ListNode(i)
        add_node(head, node)
        if i == del_node_index:
            del_node = node

    print_list(head)

    print('-----------------')

    delete_node(head, del_node)
    print_list(head)