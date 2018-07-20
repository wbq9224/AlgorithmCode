def order(push_order, pop_order):
    if push_order is None or pop_order is None:
        return False

    i = 0
    stack = []

    for ele in pop_order:
        top = len(stack)
        if top == 0 or stack[top - 1] != ele:
            while i < len(push_order) and push_order[i] != ele:
                stack.append(push_order[i])
                i += 1
            i += 1
            if i > len(push_order):
                return False
        else:
            stack.pop()

    if len(stack) == 0:
        return True

    return False


if __name__ == '__main__':
    ord1 = [1, 2, 3, 4, 5]
    ord2 = [3, 5, 4, 1, 2]
    print(order(ord1, ord2))