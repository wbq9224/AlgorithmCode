from AimOffer.ConstructBinaryTree import *

class Solution:
    def Serialize(self, root):
        # write code here
        if not root:
            return ['$']
        left = self.Serialize(root.left)
        right = self.Serialize(root.right)
        return [root.value] + left + right

    def Deserialize_core(self, s, index):
        if index >= len(s) or s[index] == '$':
            return None, index

        p_node = TreeNode(s[index], None, None)
        p_node.left, index = self.Deserialize_core(s, index + 1)
        p_node.right, index = self.Deserialize_core(s, index + 1)
        return p_node, index


    def Deserialize(self, s):
        # write code here
        return self.Deserialize_core(s, 0)[0]


if __name__ == '__main__':
    pre = [1, 2, 4, 3, 5, 6]
    in_o = [4, 2, 1, 5, 3, 6]
    root = construct(pre, in_o, 0, len(pre) - 1, 0, len(in_o) - 1)

    str = Solution().Serialize(root)
    print(str)

    root = Solution().Deserialize(str)
    post = []
    post_order_travl(root, post)
    print(post)
