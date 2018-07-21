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


if __name__ == '__main__':
    num = -123
    print(Solution().reverse(num))