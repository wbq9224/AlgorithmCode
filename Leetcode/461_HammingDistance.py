class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        exclusive_or = x ^ y
        count = 0
        while exclusive_or:
            exclusive_or = (exclusive_or - 1) & exclusive_or
            count += 1

        return count


if __name__ == '__main__':
    print(Solution().hammingDistance(1, 4))