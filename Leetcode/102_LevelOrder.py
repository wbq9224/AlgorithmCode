# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from Leetcode.AimOffer.ConstructBinaryTree import *

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        # 一种思路，每次进行层次遍历时存入该元素的层号
        # queue = [[root, 0]]
        # temp = []
        # while queue:
        #     node, level = queue.pop(0)
        #     temp.append([node.value, level])
        #     if node.left:
        #         queue.append([node.left, level + 1])
        #     if node.right:
        #         queue.append([node.right, level + 1])
        #
        # max_level = temp[-1][1]
        # res = [[] for i in range(max_level + 1)]
        #
        # for val, level in temp:
        #     res[level].append(val)
        # return res

        # 另一种思路，非常巧妙的得到每层的元素个数
        queue = [root]
        res = []
        while queue:
            temp = []
            level_ele_count = len(queue)  # 当前队列中的元素个数即为每层元素个数
            for i in range(level_ele_count):  # 此循环保证将上一层入队元素全部出队，同时将下一层元素全部入队，维护队列全部元素为下层元素
                ele = queue.pop(0)
                temp.append(ele.value)
                if ele.left:
                    queue.append(ele.left)
                if ele.right:
                    queue.append(ele.right)
            res.append(temp)
        return res


if __name__ == '__main__':
    pre = [3, 5, 6, 2, 7, 4, 1, 9, 8]
    in_o = [6, 5, 7, 2, 4, 3, 9, 1, 8]
    root = construct(pre, in_o, 0, len(pre) - 1, 0, len(in_o) - 1)

    Solution().levelOrder(root)