from AimOffer.ConstructBinaryTree import *


class Solution:
    def tin_order(self, p_node, res):
        if not p_node:
            return res

        if p_node.left:
            res = self.tin_order(p_node.left, res)
        res.append(p_node.value)
        if p_node.right:
            res = self.tin_order(p_node.right, res)
        return res

    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot:
            return
        res = self.tin_order(pRoot, [])
        print(res)
        if k >= len(res) or k <= 0:
            return
        return res[k - 1]


if __name__ == '__main__':
    pre_order = [5, 3, 2, 4, 6, 7]
    in_order = [2, 3, 4, 5, 6, 7]

    root = construct(pre_order, in_order, 0, len(pre_order) - 1, 0, len(in_order) - 1)
    Solution().KthNode(root, 1)