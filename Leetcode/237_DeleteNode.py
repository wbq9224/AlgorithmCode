# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        if not node:
            return

        if not node.next:
            del node
        else:
            temp = node.next
            node.val = temp.val
            node.next = temp.next
            del temp
        return

