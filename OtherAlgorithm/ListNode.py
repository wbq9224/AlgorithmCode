class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


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
    while p:
        print(p.data, end=' ')
        p = p.next



    print(end='\n')
