# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from Leetcode.AimOffer.ConstructBinaryTree import *


class Solution(object):
    def traverse(self, root, leaf):
        if root is None:
            return

        if not root.left and not root.right:
            leaf.append(root.val)
        if root.left:
            self.traverse(root.left, leaf)
        if root.right:
            self.traverse(root.right, leaf)
        return leaf

    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if not root1 or not root2:
            return False
        
        return self.traverse(root1, []) == self.traverse(root2, [])


if __name__ == '__main__':
    pre = [3, 5, 6, 2, 7, 4, 1, 9, 8]
    in_o = [6, 5, 7, 2, 4, 3, 9, 1, 8]
    root = construct(pre, in_o, 0, len(pre) - 1, 0, len(in_o) - 1)

    Solution().leafSimilar(root, None)