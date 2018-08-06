from AimOffer.ConstructBinaryTree import *

def convert(root):
    if root is None:
        return

    last_node = convert_node(root, TreeNode(None, None, None))  # last指向链表尾节点
    head_node = last_node

    while head_node is not None and head_node.left is not None:
        head_node = head_node.left  # 从尾结点出发找到头节点

    return head_node


def convert_node(root, last):
    p = root
    if p is None:
        return

    if p.left is not None:
        last = convert_node(p.left, last)  # 找到位于左子树最左下角的结点，为左子树最小值，同时更新last为整个左子树的尾节点

    p.left = last  # 将当前结点的前驱指向前面传过来的尾结点
    if last is not None:
        last.right = p # 将子结构的尾的后继指向当前结点
    last = p  # 将尾结点更新为当前结点
              # 注意此处，python的对象为引用传递，因此此处的last=p只是将该层递归中last的地址指向了p，原last的内容并未被修改，因此要将last返回才能更新last

    if p.right is not None:
        last = convert_node(p.right, last)  # 递归遍历连接当前结点的右子树，同时更新last使之指向更新后的尾节点
    return last


if __name__ == '__main__':
    pre_order = [10, 6, 4, 8, 14, 12, 16]
    in_order = [4, 6, 8, 10, 12, 14, 16]

    root = construct(pre_order, in_order, 0, len(pre_order) - 1, 0, len(in_order) - 1)
    head = convert(root)

    p = head.right
    while p is not None:
        print(p.value, end=' ')
        p = p.right
