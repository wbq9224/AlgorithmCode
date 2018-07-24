class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 0:
            return -1

        res = [1]
        u2 = u3 = u5 = 0
        for i in range(n - 1):
            res.append(min(res[u2] * 2, res[u3] * 3, res[u5] * 5))
            if res[u2] * 2 == res[-1]:
                u2 += 1
            if res[u3] * 3 == res[-1]:
                u3 += 1
            if res[u5] * 5 == res[-1]:
                u5 += 1

        return res[-1]


if __name__ == '__main__':
    print(Solution().nthUglyNumber(1500))