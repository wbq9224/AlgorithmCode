from Leetcode.OtherAlgorithm.ListNode import *


def reverse_list(head):
    if head is None or head.next is None:
        return

    p_node = head.next
    p_pre = None
    p_res = None

    while p_node is not None:
        p_next = p_node.next

        if p_next is None:
            p_res = ListNode(None)
            p_res.next = p_node

        p_node.next = p_pre

        p_pre = p_node
        p_node = p_next

    return p_res


if __name__ == '__main__':

    head = ListNode(None)
    for i in range(4):
        node = ListNode(i)
        add_node(head, node)

    print_list(head)

    print('-----------------')

    after_reverse_head = reverse_list(head)
    print_list(after_reverse_head)