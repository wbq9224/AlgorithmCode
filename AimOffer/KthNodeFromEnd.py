from Leetcode.AimOffer.ListNode import *


def find_kth_node_to_tail(head, k):
    # 一定要注意判断初始条件的合法性
    if head is None or k == 0:
        return

    ahead = head
    behind = head

    for i in range(k - 1):
        # 移动链表时一定要先判断下个节点是否为空
        if ahead.next is not None:
            ahead = ahead.next
        else:
            return

    while ahead.next is not None:
        ahead = ahead.next
        behind = behind.next

    print(behind.data)


if __name__ == '__main__':

    head = ListNode(None)
    for i in range(4):
        node = ListNode(i)
        add_node(head, node)

    print_list(head)

    print('-----------------')

    k = 4
    find_kth_node_to_tail(head, k)