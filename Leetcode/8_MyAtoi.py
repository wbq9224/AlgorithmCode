class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # 此题注意几点：
        # 1、使用while循环向后移动指针时一定不要忘了先判断指针是否在边界内(index < len)
        # 2、strip函数的使用：移除字符串首尾指定字符，默认为空格或换行
        # 3、经每一步处理后的字符串有可能是空串的，要先判断是否为空

        if str is None or len(str) <= 0:
            return 0

        # 处理前缀空格
        temp = str.strip()
        if len(temp) <= 0:  # 注意判断删除字符后的串是否为空
            return 0

        # 处理符号位
        negetive = -1 if temp[0] == "-" else 1
        temp = temp[1:] if temp[0] == "+" or temp[0] == "-" else temp

        # 处理数字转换
        index = 0
        while index < len(temp) and temp[index].isdigit():
            index += 1
        if index == 0:
            return 0

        # 处理溢出
        res = negetive * int(temp[:index])
        if -(2 ** 31) > res:
            return -(2 ** 31)
        elif res > 2 ** 31 - 1:
            return 2 ** 31 - 1

        return res


if __name__ == '__main__':
    # s = " "
    # s = "+"
    # s = " ++--++-1"
    # s = "   +0 123"
    # s = "-91283472332"
    # s = "   -42"
    s = "words and 987"
    # s = "4193 with words"
    print(Solution().myAtoi(s))