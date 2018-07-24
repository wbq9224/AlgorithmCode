# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 判断是否有环的思路：使用一快一慢双指针，若快指针能追上慢指针则说明有环

        if not head:
            return False

        p_fast = p_slow = head
        while p_fast and p_fast.next:
            p_fast = p_fast.next.next
            p_slow = p_slow.next

            if p_fast == p_slow:
                return True

        return False