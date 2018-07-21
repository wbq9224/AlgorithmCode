class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack is None or needle is None:
            return -1
        if len(needle) == 0:
            return 0
        if len(haystack) == 0 or len(needle) > len(haystack):
            return -1

        # 方法一：暴力法
        # i = 0
        # while i < len(haystack) - len(needle) + 1:
        #     j = 0
        #     if haystack[i] == needle[j]:
        #         temp = i
        #         while temp < len(haystack) and j < len(needle) and haystack[temp] == needle[j]:
        #             j += 1
        #             temp += 1
        #         if j == len(needle):
        #             return i
        #     i += 1

        # 方法二：方法一的切片版，但效率高很多
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: i + len(needle)] == needle:
                return i

        # 方法三：KMP，太复杂

        return -1


if __name__ == '__main__':
    haystack = "hello"
    needle = "ll"
    # haystack = "aaaaa"
    # needle = "bba"
    print(Solution().strStr(haystack, needle))