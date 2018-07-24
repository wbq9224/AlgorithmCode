# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from Leetcode.AimOffer.ListNode import *


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 方法一：递归
        # if not l1:
        #     return l2
        # if not l2:
        #     return l1
        #
        # p = ListNode(None)
        # if l1.data < l2.data:
        #     p = l1
        #     p.next = self.mergeTwoLists(l1.next, l2)
        # else:
        #     p = l2
        #     p.next = self.mergeTwoLists(l1, l2.next)
        # return p

        # 方法二：循环
        p_head = p = ListNode(0)
        while l1 and l2:
            if l1.data < l2.data:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        p.next = l1 or l2
        return p_head.next


if __name__ == '__main__':
    head1 = ListNode(None)
    head2 = ListNode(None)
    for i in range(0, 10, 2):
        node = ListNode(i)
        add_node(head1, node)
    for i in range(1, 11, 2):
        node = ListNode(i)
        add_node(head2, node)

    print_list(head1)
    print_list(head2)

    print('-----------------')

    p = Solution().mergeTwoLists(head1.next, head2.next)

    new_head = ListNode(None)
    new_head.next = p
    print_list(new_head)
