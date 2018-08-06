class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        # 中心扩展法，但要考虑长度为奇或偶两种情况
        # 如aba，即以b为中心向两边扩展；若为abba，则以bb为中心向两边扩展
        max_s, max_e = 0, 0
        for i, c in enumerate(s):
            len1 = self.expand(s, i, i)
            len2 = self.expand(s, i, i + 1)
            temp = max(len1, len2)
            if temp > (max_e - max_s):
                max_s = i - ((temp - 1) >> 1)
                max_e = i + (temp >> 1)

        return s[max_s: max_e + 1]

    def expand(self, s, left, right):
        while left >=0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1


if __name__ == '__main__':
    string = "babad"
    print(Solution().longestPalindrome(string))
