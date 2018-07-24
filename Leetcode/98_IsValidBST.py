# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def in_order_traverse(self, root, sorted_num):
        if not root:
            return

        if root.left:
            self.in_order_traverse(root.left, sorted_num)
        sorted_num.append(root.val)
        if root.right:
            self.in_order_traverse(root.right, sorted_num)
        return

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if not root:
            return True

        # 根据bst中序遍历必为有序数列的特点，对其进行验证即可
        number = []
        self.in_order_traverse(root, number)

        for i in range(len(number) - 1):
            if number[i] >= number[i + 1]:
                return False

        return True
