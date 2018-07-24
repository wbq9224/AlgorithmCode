# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def symmetric(self, root1, root2):
        # 若为叶结点则必对称
        if not root1 and not root2:
            return True
        # 若有一个为空则必不对称
        if not root1 or not root2:
            return False
        # 判断两子树是否对称相等，即判断树1的左子树是否等于树2的右子树，树1的右子树是否等于树2的左子树
        return root1.val == root2.val and self.symmetric(root1.left, root2.right) and self.symmetric(root1.right, root2.left)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        # 方法一：递归，此思路还可用于判断两二叉树是否相等
        # return self.symmetric(root.left, root.right)

        # 方法二：迭代，利用栈去保存每一步状态，即树1的左子树，树2的右子树，树1的右子树，树2的左子树
        stack = [root.left, root.right]
        while stack:
            p = stack.pop()
            q = stack.pop()

            if not p and not q:
                continue
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            stack.append(p.left)
            stack.append(q.right)
            stack.append(p.right)
            stack.append(q.left)

        return True


