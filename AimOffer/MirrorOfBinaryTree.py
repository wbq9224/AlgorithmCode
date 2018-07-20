from Leetcode.AimOffer.ConstructBinaryTree import *


def mirror_tree(node):
    if node is None:
        return

    if node.left is None and node.right is None:
        return

    temp = node.left
    node.left = node.right
    node.right = temp
    if node.left is not None:
        mirror_tree(node.left)
    if node.right is not None:
        mirror_tree(node.right)


if __name__ == '__main__':
    pre_order = np.array([
        5, 3, 2, 4, 6, 7
    ])
    in_order = np.array([
        2, 3, 4, 5, 6, 7
    ])

    root = construct(pre_order, in_order, 0, len(pre_order) - 1, 0, len(in_order) - 1)

    post_1 = []
    post_order_travl(root, post_1)
    print(post_1)

    post_2 = []
    mirror_tree(root)
    post_order_travl(root, post_2)
    print(post_2)