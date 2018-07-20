from Leetcode.AimOffer.ListNode import *


def merge_list(head1, head2):
    if head1 is None and head2 is None:
        return

    if head1 is None:
        return head2
    if head2 is None:
        return head1

    p = head1 if head1.data < head2.data else head2
    p.next = merge_list(head1.next, head2) if head1.data < head2.data else merge_list(head1, head2.next)

    return p


if __name__ == '__main__':
    list1_head = ListNode(None)
    for i in range(0, 10, 2):
        p = ListNode(i)
        add_node(list1_head, p)

    list2_head = ListNode(None)
    for i in range(1, 11, 2):
        p = ListNode(i)
        add_node(list2_head, p)

    print_list(list1_head)
    print_list(list2_head)

    print('-------------')

    new_head = ListNode(None)
    new_head.next = merge_list(list1_head.next, list2_head.next)
    print_list(new_head)