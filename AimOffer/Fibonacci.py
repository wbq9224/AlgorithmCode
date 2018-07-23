def fibonacci(n):
    if 0 <= n < 2:
        return n

    n0 = 0
    n1 = 1
    print(n1)
    for i in range(2, n + 1):
        # 直接代码
        # n1 = n0 + n1
        # n0 = n1 - n0

        # python代码1
        n0, n1 = n1, n0 + n1

        print(n1)
    return n1


# python代码2：生成器
def fib_2(n):
    index, n0, n1 = 0, 0, 1
    while index < n:
        yield n1  # 生成器的用法
        n0, n1 = n1, n0 + n1
        index += 1
    return


if __name__ == '__main__':
    n = int(input())
    fibonacci(n)
    print("------------")
    for fi in fib_2(n):
        print(fi)





