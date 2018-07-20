'''
    常用位操作：
    &按位与，|按位或，^按位异或，~按位取反
    >> 1等价于除以2， << 1等价于乘以2
    原数-1 & 原数） 等价于把原数二进制的最右端的1变为0
    故该方法还可用来判断一个数是不是2的整数次方（2的整数次方的数的二进制中有且只有一位是1）
    & 0x1等价于求余%
'''


def number_of_one(num):
    count = 0
    while num != 0:
        count += 1
        num = (num - 1) & num

    return count


if __name__ == '__main__':
    print(number_of_one(521))