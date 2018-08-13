class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead:
            return

        p_ahead, p_behind = pHead, pHead
        circle_flag, circle_nodes = False, 1
        while p_ahead and p_ahead.next:
            p_ahead = p_ahead.next.next
            p_behind = p_behind.next

            if p_ahead == p_behind:
                circle_flag = True
                p_behind = p_behind.next
                while p_behind != p_ahead:
                    circle_nodes += 1
                    p_behind = p_behind.next
                break

        if circle_flag:
            p_ahead, p_behind = pHead, pHead
            for i in range(circle_nodes):
                p_ahead = p_ahead.next
            while p_ahead != p_behind:
                p_ahead = p_ahead.next
                p_behind = p_behind.next
            return p_ahead
        return