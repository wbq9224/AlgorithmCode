def find_duplication(num):
    if not num:
        return

    n = len(num)
    for i in range(n):
        if num[i] >= n or num[i] < 0:
            return

    # 方法一：排序，时间复杂度Onlogn
    # 方法二：hash，空间复杂度On
    # 方法三：利用数字在0~n-1这一特性，时间复杂度On，空间复杂度O1
    for i in range(n):
        if num[i] != i:
            while num[i] != i:
                index = num[i]
                if num[index] == num[i]:
                    return num[i]

                num[i] = num[i] ^ num[index]
                num[index] = num[i] ^ num[index]
                num[i] = num[i] ^ num[index]
    return


if __name__ == '__main__':
    number = [2, 3, 1, 0, 2, 5, 3]
    print(find_duplication(number))