class ComplexListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.sibling = None


def add_node(head, node):
    if head is None or node is None:
        return

    p = head
    while p.next is not None:
        p = p.next
    p.next = node
    return head


def print_list(head):
    if head is None:
        return

    p = head
    while p.next is not None:
        p = p.next
        print(p.value, end=' ')

    print(end='\n')


def copy_complex_list(head):  # 分三步复制复杂链表
    if head is None:
        return

    # 复制原链表结点至原结点后
    p = head.next
    while p is not None:
        copy = ComplexListNode(p.value)
        copy.next = p.next
        p.next = copy

        p = copy.next

    # 复制指向任意结点的指针
    p = head.next
    while p is not None:
        copy = p.next
        if p.sibling is not None:
            copy.sibling = p.sibling.next
        p = copy.next

    # 拆分原链表与复制链表
    p = head.next
    new_head = ComplexListNode(None)
    new_p = None
    if p is not None:
        new_head.next = new_p = p.next
        p.next = new_p.next
        p = p.next
    while p is not None:
        new_p.next = p.next
        new_p = new_p.next
        p.next = new_p.next
        p = p.next

    return new_head


if __name__ == '__main__':
    head = ComplexListNode(None)
    for i in range(4):
        node = ComplexListNode(i)
        add_node(head, node)

    print_list(head)

    copy_head = copy_complex_list(head)
    print_list(copy_head)

