class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if s is None or t is None or len(s) != len(t):
            return False

        # 方法一：对比原字符串转ascii排序后的序列看是否一致，O（nlogn）
        # temp_s = list(map(ord, s))
        # temp_t = list(map(ord, t))
        # temp_s.sort()
        # temp_t.sort()
        # return temp_s == temp_t

        # 方法二：利用set获得s中所有不重复的字母后统计每个字母在t中出现的次数，这个方法要注意判断s与t是否等长
        for ch_s in set(s):
            if s.count(ch_s) != t.count(ch_s):
                return False
        return True


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    print(Solution().isAnagram(s, t))