# 求树的深度
def tree_depth(root):
    if not root:
        return 0

    left = tree_depth(root.left)
    right = tree_depth(root.right)
    return max(left, right) + 1


# 判断是否为平衡二叉树
def is_balanced_tree(root):
    if not root:
        return 0, True

    left_depth, left_flag = is_balanced_tree(root.left)
    right_depth, right_flag = is_balanced_tree(root.right)
    if left_flag and right_flag and abs(left_depth - right_depth) <= 1:
        return max(left_depth, right_depth) + 1, True
    return max(left_depth, right_depth) + 1, False
