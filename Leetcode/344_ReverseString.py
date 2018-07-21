class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None:
            return

        # 方法一
        res = "".join(list(s)[::-1])

        # 方法二：从两端向中间做交换，值得注意的是这种不需要辅助空间的交换两数的方法
        # length = len(s)
        # str_list = list(map(ord, s))
        # for i in range(length >> 1):
        #     str_list[i] = str_list[i] ^ str_list[length - i - 1]
        #     str_list[length - i - 1] = str_list[i] ^ str_list[length - i - 1]
        #     str_list[i] = str_list[i] ^ str_list[length - i - 1]
        # res = "".join(map(chr, str_list))
        return res


if __name__ == '__main__':
    s = "hello"
    print(Solution().reverseString(s))