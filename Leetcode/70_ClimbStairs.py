class Solution(object):
    # 使用生成器
    def fibonacci(self, n):
        t, n1, n2 = 0, 1, 1
        while t < n:
            yield n2
            n2, n1 = n1 + n2, n2
            t += 1

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        n1, n2, t = 1, 1, 1
        while t < n:
            n2, n1 = n1 + n2, n2
            t += 1
        return n2


if __name__ == '__main__':
    print(Solution().climbStairs(5))