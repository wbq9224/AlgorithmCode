from OtherAlgorithm.ListNode import *


class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead:
            return

        p_node = ListNode(None)
        p_node.next = pHead
        p1, p2 = p_node, p_node.next

        while p2:
            p2 = p2.next
            if p2 and p1.next.val != p2.val:
                if p1.next.next == p2:
                    p1 = p1.next
                else:
                    p1.next = p2
        if p1.next.next != p2:
            p1.next = p2
        return p_node.next


if __name__ == '__main__':
    head = ListNode(None)
    for i in range(5):
        new_node = ListNode(i)
        add_node(head, new_node)
        new_node = ListNode(i)
        add_node(head, new_node)

    print_list(head.next)
    head = Solution().deleteDuplication(head.next)

    print_list(head)