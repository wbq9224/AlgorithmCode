
def replace(str):
    if str is None:
        return

    blank_count = 0
    for char in str:
        if char == ' ':
            blank_count += 1

    rear_after_replace = 2 * blank_count + len(str)
    rear = len(str)

    new = ['' for i in range(rear_after_replace)]
    for i in range(rear, 0, -1):
        if str[i - 1] != ' ':
            new[rear_after_replace - 1] = str[i - 1]
            rear_after_replace -= 1
        else:
            new[rear_after_replace - 1] = '0'
            rear_after_replace -= 1
            new[rear_after_replace - 1] = '2'
            rear_after_replace -= 1
            new[rear_after_replace - 1] = '%'
            rear_after_replace -= 1

    return "".join(new)


if __name__ == '__main__':
    a = "ab c defg"
    b = ""
    c = " "
    d = "  "
    e = "abc "
    f = " abc"
    g = None
    print(replace(g))
