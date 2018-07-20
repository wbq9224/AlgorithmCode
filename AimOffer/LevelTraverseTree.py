from Leetcode.AimOffer.ConstructBinaryTree import *
from Leetcode.AimOffer.QueueWithTwoStack import *


def level_traverse(root):
    if not root:
        return

    queue = Queue()
    queue.append_tail(root)

    while queue.get_size():
        head = queue.delete_head()
        print(head.value, end=' ')

        if head.left:
            queue.append_tail(head.left)
        if head.right:
            queue.append_tail(head.right)

    return


if __name__ == '__main__':
    pre_order = np.array([
        5, 3, 2, 4, 6, 7
    ])
    in_order = np.array([
        2, 3, 4, 5, 6, 7
    ])

    root = construct(pre_order, in_order, 0, len(pre_order) - 1, 0, len(in_order) - 1)

    level_traverse(root)
