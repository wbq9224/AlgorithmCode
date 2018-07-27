class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        count = 0
        while n != 0:
            n = (n - 1) & n
            count += 1

        return count

if __name__ == '__main__':
    print(Solution().hammingWeight(11))