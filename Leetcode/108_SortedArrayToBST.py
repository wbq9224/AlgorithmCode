# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from AimOffer.ConstructBinaryTree import *


class Solution(object):
    # def construct_BST(self, key, root):
    #     if not root:
    #         return TreeNode(key, None, None)
    #     if root.value == key:
    #         return root
    #     if key < root.value:
    #         root.left = self.construct_BST(key, root.left)
    #     else:
    #         root.right = self.construct_BST(key, root.right)
    #     return root

    def construct_bst(self, nums, left, right):
        if left > right:
            return

        mid = (left + right) >> 1
        node = TreeNode(nums[mid], None, None)
        node.left = self.construct_bst(nums, left, mid - 1)
        node.right = self.construct_bst(nums, mid + 1, right)
        return node

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        # 本体思路：若使用顺序插入每个元素完成二叉排序树的插入+构造，则需单独考虑平衡问题比较麻烦，且没有利用数组是顺序这一特性
        # 比较好的思路：利用顺序特性，采用二分插入，每次插入中间结点，递归实现，能保证完成插入+构造的同时保证平衡问题
        # 但也要学会一般的二叉排序树的构造方法

        if not nums:
            return

        # root = None
        # for num in nums:
        #     root = self.construct_BST(num, root)

        return self.construct_bst(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    num = [16, 3, 7, 11, 9, 26, 18, 14, 15]
    root = Solution().sortedArrayToBST(num)

    in_order = []
    in_order_travl(root, in_order)
    print(in_order)