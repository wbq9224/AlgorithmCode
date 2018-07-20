from Leetcode.AimOffer.ConstructBinaryTree import *


def visit(node, key, path):
    path.append(node.value)
    if node.left is None and node.right is None and sum(path) == key:
        print(path)


def find_path(root, key, path):
    if root is None:
        return

    visit(root, key, path)
    if root.left is not None:
        find_path(root.left, key, path)
    if root.right is not None:
        find_path(root.right, key, path)

    path.pop()


if __name__ == '__main__':
    pre_order = [5, 7, 2, 4, 6, 1]
    in_order = [2, 7, 4, 5, 6, 1]

    root = construct(pre_order, in_order, 0, len(pre_order) - 1, 0, len(in_order) - 1)

    find_path(root, 13, [])