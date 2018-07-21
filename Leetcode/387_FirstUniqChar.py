class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None:
            return -1

        # 方法一：hash
        # ch_temp = list(map(ord, s))
        # d = {}
        # for ch in ch_temp:
        #     d[ch] = d.get(ch, 0) + 1
        # for index, ch in enumerate(ch_temp):
        #     if d[ch] == 1:
        #         return index
        # return -1

        # 方法二：由于输入限定为小写字母，因此可遍历26个字母在输入中最先和最后出现的位置，若相等则说明无重复，最后取最小的一个即可
        min_index = len(s)
        low_alpha = "abcdefghijklmnopqrstuvwxyz"
        for ch in low_alpha:
            f_index = s.find(ch)
            l_index = s.rfind(ch)
            if f_index == l_index and f_index != -1:
                min_index = min(min_index, f_index)
        return min_index if min_index != len(s) else -1


if __name__ == '__main__':
    s = "loveleetcode"
    print(Solution().firstUniqChar(s))