import random
from Leetcode.OtherAlgorithm.ListNode import *


# 使用递归完成继续输出单链表
def anti_print(node):
    if node.next is not None :
        anti_print(node.next)
    if node.data is not None:
        print(node.data, end=' ')
    return


if __name__ == '__main__':
    head = ListNode(None)
    for i in range(10):
        new_node = ListNode(random.randint(-100, 100))
        add_node(head, new_node)

    # 正序输出
    print_list(head)

    print('-------')

    # 倒序输出
    anti_print(head)