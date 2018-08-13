from OtherAlgorithm.ListNode import *

if __name__ == '__main__':
    head = ListNode(None)
    for i in range(10):
        new_node = ListNode(i)
        add_node(head, new_node)

    # 正序输出
    print_list(head)

    p1 = head.next
    p2 = p1

    p1 = p1.next
    print(p1.data)
    print(p2.data)