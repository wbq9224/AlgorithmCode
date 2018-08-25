# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        level_index = 1
        queue, res = [pRoot], []
        while len(queue):
            count = len(queue)
            level = []
            for i in range(count):
                p_node = queue.pop(0)
                level.append(p_node.val)
                if p_node.left:
                    queue.append(p_node.left)
                if p_node.right:
                    queue.append(p_node.right)
            level_index += 1
            if level_index & 1 == 1:
                res.append(level[::-1])
            else:
                res.append(level)
        return res
