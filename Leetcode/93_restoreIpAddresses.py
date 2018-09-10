class Solution(object):
    def is_vaild(self, s):
        if s == '0':
            return True
        elif s[0] == '0':
            return False

        return 0 < int(s) <= 255

    def dfs(self, index, temp_count, s, temp_res, res):
        if temp_count == 4:
            res.append("".join(temp_res[:-1]))
            return
        else:
            for i in range(1, 4):
                if len(s) - 3 * (3 - temp_count) <= index + i <= len(s):
                    temp = s[index: index + i]
                    if self.is_vaild(temp):
                        temp_res.append(temp)
                        temp_res.append('.')
                        self.dfs(index + i, temp_count + 1, s, temp_res, res)
                        temp_res.pop()
                        temp_res.pop()
        return

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        if not s or len(s) < 4 or len(s) > 12:
            return []

        res, temp_res = [], []
        self.dfs(0, 0, s, temp_res, res)

        return res


if __name__ == '__main__':
    ip = "25525511135"
    print(Solution().restoreIpAddresses(ip))