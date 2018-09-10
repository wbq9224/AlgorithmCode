class TreeNode:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


def construct(pre_order, in_order, start_pre, end_pre, start_in, end_in):
    if pre_order is None or in_order is None or end_pre - start_pre < 0 or end_in - start_in < 0:
        return

    root_value = pre_order[start_pre]
    root_node = TreeNode(root_value, None, None)

    if start_pre == end_pre and start_in == end_in:
        return root_node

    root_in_in_order = -1
    for i in range(start_in, end_in + 1):
        if in_order[i] == root_value:
            root_in_in_order = i
            break

    if root_in_in_order == -1:
        raise ValueError("can not find value in in_order")
    else:
        left_length = root_in_in_order - start_in
        left_pre_end = start_pre + left_length
        if left_length > 0:
            root_node.left = construct(pre_order, in_order, start_pre + 1, left_pre_end, start_in, root_in_in_order - 1)
        if left_length < (end_pre - start_pre):
            root_node.right = construct(pre_order, in_order, left_pre_end + 1, end_pre, root_in_in_order + 1, end_in)

    return root_node


def post_order_travl(root, post_order):
    if root is None:
        return

    if root.left is not None:
        post_order_travl(root.left, post_order)
    if root.right is not None:
        post_order_travl(root.right, post_order)

    post_order.append(root.value)

    return


def in_order_travl(root, in_order):
    if root is None:
        return

    if root.left is not None:
        in_order_travl(root.left, in_order)

    in_order.append(root.value)

    if root.right is not None:
        in_order_travl(root.right, in_order)

    return


if __name__ == '__main__':

    pre_order = [4, 3, 9, 7, 6, 5, 8, 1, 2]
    in_order = [7, 9, 6, 3, 5, 4, 1, 8, 2]

    root = construct(pre_order, in_order, 0, len(pre_order) - 1, 0, len(in_order) - 1)

    post_order = []
    post_order_travl(root, post_order)
    print(post_order)

