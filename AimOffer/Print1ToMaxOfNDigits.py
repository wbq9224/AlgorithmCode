def print_1_to_max_of_n_digits(n):
    if n <= 0:
        return

    num = ['0' for i in range(n)]
    for i in range(10):
        num[0] = str(i)
        recisively(num, 0)


def recisively(num, index):
    if index == len(num) - 1:
        begin = 0
        while begin <= index:
            if num[begin] != '0':
                break
            begin += 1
        if begin > index:
            begin = index
        print(''.join(num[begin:]))
        return

    for i in range(10):
        num[index + 1] = str(i)
        recisively(num, index + 1)


if __name__ == '__main__':
    n = 5

    print_1_to_max_of_n_digits(n)
