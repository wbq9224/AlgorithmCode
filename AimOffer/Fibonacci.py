def fibonacci(n):
    if 0 <= n < 2:
        return n

    n0 = 0
    n1 = 1
    n2 = 0
    for i in range(2, n + 1):
        n2 = n0 + n1
        n0 = n1
        n1 = n2
    return n2


if __name__ == '__main__':
    n = int(input())
    print(fibonacci(n))






