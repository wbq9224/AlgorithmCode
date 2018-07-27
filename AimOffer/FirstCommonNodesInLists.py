from Leetcode.OtherAlgorithm.ListNode import *


def find_first_common_node(head1, head2):
    if not head1 or not head2:
        return -1

    p1, p2 = head1, head2
    l1, l2 = 0, 0
    while p1:
        p1 = p1.next
        l1 += 1
    while p2:
        p2 = p2.next
        l2 += 1

    print(l1, l2)
    p = head1 if l1 > l2 else head2
    q = head2 if l2 <= l1 else head1
    for i in range(abs(l1 - l2)):
        p = p.next

    while p and q and p != q:
        if p == q:
            return q.data
        p = p.next
        q = q.next

    return -1


if __name__ == '__main__':
    # test
    list1_head = ListNode(None)
    for i in range(0, 14, 2):
        p = ListNode(i)
        add_node(list1_head, p)

    list2_head = ListNode(None)
    for i in range(1, 11, 3):
        p = ListNode(i)
        add_node(list2_head, p)

    p = ListNode(13)
    add_node(list1_head, p)
    add_node(list2_head, p)

    for i in range(0, 4, 2):
        p = ListNode(i)
        add_node(list1_head, p)

    print_list(list1_head)
    print_list(list2_head)

    print(find_first_common_node(list1_head.next, list2_head.next))