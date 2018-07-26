# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from Leetcode.OtherAlgorithm.ListNode import *

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        # 分三种情况：
        # 1，待删除结点是非头非尾结点（一般情况，即 n > 1）
        # 2，待删除结点是长度大于1的链表的尾节点（即n == 1）
        # 3，待删除结点是长度等于1的链表的尾节点（也即头节点, n == 1）
        # 针对1，则先让i走k-1，ij再同时走直到i走到尾，则j指向待删除结点，利用后一元素覆盖法直接删去即可
        # 针对2，此时无法使用后一元素覆盖法，只能用前驱去删，因此需要让j走到待删元素的前驱处，因此在初始时让j位于i前驱处即可
        # 针对3，则需将头结点修改为空

        if not head or n <= 0:
            return head

        if n == 1:
            pi = head
            pj = ListNode(0)
            pj.next = head
        else:
            pj = pi = head

        for i in range(n - 1):
            if pi:
                pi = pi.next
            else:
                return head

        while pi.next:
            pi = pi.next
            pj = pj.next

        if n == 1 and head == pi:
            return None
        if n == 1:
            pj.next = pj.next.next
        else:
            pj.data = pj.next.data
            pj.next = pj.next.next

        return head


if __name__ == '__main__':
    head = ListNode(None)
    for i in range(1):
        node = ListNode(i + 1)
        add_node(head, node)

    print_list(head)

    print('-----------------')

    p = Solution().removeNthFromEnd(head.next, 1)
    new_head = ListNode(None)
    new_head.next = p
    print_list(new_head)