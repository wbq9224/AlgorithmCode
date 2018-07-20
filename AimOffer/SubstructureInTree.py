from Leetcode.AimOffer.ConstructBinaryTree import *


def find_sub_tree(train_root, query_root):
    flag = False
    if train_root is None or query_root is None:
        return flag

    if train_root.value == query_root.value:
        flag = find_son(train_root, query_root)
    if not flag:
        flag = find_sub_tree(train_root.left, query_root)
        flag = find_sub_tree(train_root.right, query_root)

    return flag


def find_son(train_root, query_root):
    # 注意此处要将字串的判断放在前
    if query_root is None:
        return True
    # 主串的判断放在后
    if train_root is None:
        return False
    if train_root.value != query_root.value:
        return False

    return find_son(train_root.left, query_root.left) and find_son(train_root.right, query_root.right)


if __name__ == '__main__':
    a_pre = np.array([1, 2, 4, 7, 3, 5, 6, 8])
    a_in = np.array([4, 7, 2, 1, 5, 3, 8, 6])
    root = construct(pre_order=a_pre, in_order=a_in,
                     start_pre=0, end_pre=len(a_pre) - 1,
                     start_in=0, end_in=len(a_in) - 1)
    root2 = construct(pre_order=a_pre, in_order=a_in,
                     start_pre=0, end_pre=len(a_pre) - 1,
                     start_in=0, end_in=len(a_in) - 1)

    print(find_sub_tree(root, root2))