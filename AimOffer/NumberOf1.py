if __name__ == '__main__':
    n = 123

    i = 1
    count = 0

    while i <= n:
        a = int(n / i)
        b = n % i
        count += (a + 8) / 10 * i + (a % 10 == 1) * (b + 1)
        i *= 10

    print(count)