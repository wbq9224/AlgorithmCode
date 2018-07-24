import functools

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not nums:
            return ""

        # 注意join的用法并非是直接连接两字符串！
        # python3中取消了cmp函数，需要用functools实现其功能
        # cmp函数：返回正代表s1>s2,负表示s1<s2
        # 此处比较的是连接后的字符串所表示的大小，即若s1s2>s2s1，则说明s2应排在s1前，也即s1>s2

        str_nums = list(map(str, nums))
        comp = lambda s1, s2: 1 if s1 + s2 > s2 + s1 else -1
        sorted_nums = sorted(str_nums, key=functools.cmp_to_key(comp), reverse=True)
        return str(int("".join(sorted_nums)))


if __name__ == '__main__':
    nums = [3, 32, 321]
    print(Solution().largestNumber(nums))