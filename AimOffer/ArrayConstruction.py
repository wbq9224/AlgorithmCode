def constructe_b(a):
    if not a:
        return []

    # 将b看作由a[0]*a[1]*...*a[i-1]与a[i+1]*a[i+2]*...*a[n-1]两部分
    # 则前一部分可由自顶向下累乘算出，后一部分可由自底向上累乘算出,时间复杂度On

    n = len(a)
    b = [1]
    for i in range(1, n):
        b.append(b[i - 1] * a[i - 1])
    temp = 1
    for i in range(n - 2, -1, -1):
        temp *= a[i + 1]
        b[i] *= temp
    return b


if __name__ == '__main__':
    a = [5, 4, 3, 2, 1]
    print(constructe_b(a))
