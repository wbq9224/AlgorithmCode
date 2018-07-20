def my_pow(x, y):
    # 注意double类型数相等的判断，为两数绝对值小于某一阈值即可认为相等
    double_thre = 1e-6
    if abs(x - 0.0) < double_thre and x < 0:
        raise ValueError("base number can not be zero")  # 处理底数为0，指数为负的情况

    res = power(x, abs(y))
    if y < 0:
        res = 1 / res  # 处理指数为负的情况
    return res


def power(x, y):
    # 递归边界处理
    if y == 0:
        return 1
    if y == 1:
        return x

    # 使用公式a ** n = a ** (n / 2) * a ** (n / 2)递归计算a**n（n为偶数时）
    res = power(x, y >> 1)  # 这里使用 >> 1等价除以2
    res *= res
    # n为奇数时则再乘上一个底数
    if y & 0x1 == 1:  # 这里使用 &0x1等价于求余
        res *= x
    return res


if __name__ == '__main__':
    x = 2.00000
    y = 10
    print(my_pow(x, y))