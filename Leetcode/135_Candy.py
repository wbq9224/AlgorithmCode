class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings:
            return 0

        n = len(ratings)
        candys = [1 for _ in range(n)]

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candys[i] = candys[i - 1] + 1
        for i in range(n - 1, 0, -1):
            if ratings[i - 1] > ratings[i] and candys[i - 1] <= candys[i]:
                candys[i - 1] = candys[i] + 1

        return sum(candys)


if __name__ == '__main__':
    r = [1, 0, 2]
    print(Solution().candy(r))