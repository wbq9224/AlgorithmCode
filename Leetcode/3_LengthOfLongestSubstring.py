class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        # 利用hash维护一个滑动窗口，使窗口内无重复字符
        # 用cur_left记下当前滑动窗口的左边界，遍历右边界
        # 当hash中无当前字符时，记下当前字符位置并更新最大长度
        # 当hash中已有当前字符时，且当前字符的上一次出现位置位于滑动窗口内，则将当前滑动窗口左边界更新为当前字符的上一次出现位置+1
        # 更新当前字符的最新位置

        hash_table = {}
        max_len = -1
        cur_left = 0

        for i, char in enumerate(s):
            if char in hash_table and cur_left <= hash_table[char]:
                cur_left = hash_table[char] + 1
            else:
                max_len = max(max_len, i - cur_left + 1)
            hash_table[char] = i

        return max_len


if __name__ == '__main__':
    string = "abcabcbb"
    Solution().lengthOfLongestSubstring(string)