class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if strs is None or len(strs) == 0:
            return ""

        # 方法一：直接法，注意min的用法
        # # min_len = min([len(s) for s in strs])
        # min_str = min(strs, key=len)
        # for i, ch in enumerate(min_str):
        #     for s in strs:
        #         if s[i] != ch:
        #             return s[:i]
        #
        # return min_str

        # 方法二：利用zip，注意zip(str)与zip(*str)的用法
        ans = ""
        for i in zip(*strs):
            if len(set(i)) > 1:
                return ans
            ans += i[0]
        return ans


if __name__ == '__main__':
    # s = ["dog","racecar","car"]
    # s = ["","",""]
    s = ["flower","flow","flight"]
    print(Solution().longestCommonPrefix(s))