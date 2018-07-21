class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0:
            return ""
        if n == 1:
            return "1"

        s = ["1"]
        for i in range(n - 1):
            count = 1
            temp = []
            for j in range(len(s) - 1):
                if s[j] != s[j + 1]:
                    temp.append(str(count))
                    temp.append(s[j])
                    count = 1
                else:
                    count += 1
            temp.append(str(count))
            temp.append(s[-1])
            s = temp[:]

        return "".join(s)


if __name__ == '__main__':
    n = 6
    print(Solution().countAndSay(n))