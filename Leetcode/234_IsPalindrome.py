# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from Leetcode.OtherAlgorithm.ListNode import *


class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        # 方法一：先顺序遍历，将链表反转后再倒叙遍历，对比结果
        # p = head
        # forward = []
        # while p:
        #     forward.append(p.val)
        #     p = p.next
        #
        # p, p_pre = head, None
        # while p:
        #     p_next = p.next
        #     p.next = p_pre
        #     p_pre = p
        #     p = p_next
        #
        # back = []
        # p = p_pre
        # while p:
        #     back.append(p.val)
        #     p = p.next
        # return forward == back
        #
        # 方法二：先顺序遍历，然后用切片逆序后比对
        # p = head
        # temp_list = []
        # while p:
        #     temp_list.append(p.val)
        #     p = p.next
        # return temp_list == temp_list[::-1]
        #
        # 方法三：以上两种方法均不满足空间为O1的要求，下面这种方法可以做到。
        # 即将原链表从中间断开，然后原地反转后半部分链表，最后比对两部分即可
        p_fast, p_slow = head.next, head  # 注意此处的处理，快指针要比慢指针先走一步
        while p_fast and p_fast.next:
            p_fast = p_fast.next.next
            p_slow = p_slow.next

        p, p_pre = p_slow.next, None
        p_slow.next = None  # 从中间断开

        while p:  # 反转
            p_next = p.next
            p.next = p_pre
            p_pre = p
            p = p_next

        p = head  # 从两端向中间依次对比
        while p and p_pre:
            if p.data != p_pre.data:
                return False
            p = p.next
            p_pre = p_pre.next
        return True


if __name__ == '__main__':
    head = ListNode(None)
    for i in range(2):
        node = ListNode(i + 1)
        add_node(head, node)

    print_list(head)
    print(Solution().isPalindrome(head.next))