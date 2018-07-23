from functools import reduce


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        str_x = str(x)
        if str_x[0] == "-":
            str_x = str_x.replace("-", "")
            res = -int(str_x[::-1])
        else:
            res = int(str_x[::-1])

        if res > 2 ** 31 - 1 or res < - (2 ** 31):
            return 0

        return res


# 另附：map/reduce函数组合实现str->int
def str_to_int(s):
    DIGIT = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return reduce(lambda x, y: x * 10 + y, map(lambda x: DIGIT[x], s))


if __name__ == '__main__':
    num = -123
    print(Solution().reverse(num))
