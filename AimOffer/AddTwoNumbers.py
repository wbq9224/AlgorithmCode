def add(num1, num2):
    while num2:
        e_o = num1 ^ num2  # 两数异或等价于两数相加但不进位
        carry = (num1 & num2) << 1  # 两数做与即计算出要产生进位的位，左移即将此为进上

        num1 = e_o
        num2 = carry

    return num1


if __name__ == '__main__':
    print(add(3, 20))