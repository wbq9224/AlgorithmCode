class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        if not s:
            return

        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        to_int_list = list(map(lambda x: dict[x], s))
        res = 0
        for i in range(len(to_int_list) - 1):
            if to_int_list[i] >= to_int_list[i + 1]:
                res += to_int_list[i]
            else:
                res -= to_int_list[i]

        return res + to_int_list[-1]


if __name__ == '__main__':
    s = 'MCMXCIV'
    Solution().romanToInt(s)