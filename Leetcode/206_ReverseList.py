# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from Leetcode.OtherAlgorithm.ListNode import *


class Solution:
    def reverse(self, node):
        if not node.next:
            return node
        else:
            p_next = node.next  # 拿到当前结点的next
            p_head = self.reverse(p_next)  # 递归反转剩余结点
            p_next.next = node  # 将当前结点的next的next指向当前结点（即反转）
            node.next = None  # 将当前结点的next指向空
            return p_head

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        # 方法一：循环, 比较直观
        # p_pre, p_curr = None, head
        # while p_curr:
        #     p_next = p_curr.next  # 先拿到当前结点的next，防止链表断裂
        #
        #     p_curr.next = p_pre  # 将当前结点的next指向其前驱
        #
        #     p_pre = p_curr  # 移动前驱
        #     p_curr = p_next  # 移动链表

        # 方法二：递归, 比较难理解
        return self.reverse(head)


if __name__ == '__main__':
    head = ListNode(None)
    for i in range(5):
        node = ListNode(i + 1)
        add_node(head, node)

    print_list(head)

    print('-----------------')

    p = Solution().reverseList(head.next)

    new_head = ListNode(None)
    new_head.next = p
    print_list(new_head)