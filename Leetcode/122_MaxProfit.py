class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None:
            return 0

        days = len(prices)
        if days < 2:
            return 0

        # profit = [prices[i + 1] - prices[i] for i in range(days - 1)]
        # sum(filter(lambda x: x > 0, profit))

        profit = [prices[i + 1] - prices[i] for i in range(days - 1) if prices[i + 1] - prices[i] > 0]

        return sum(profit)


if __name__ == '__main__':
    # a = [7, 1, 5, 3, 6, 4]
    a = [7, 6, 5, 4, 3, 2]

    so = Solution()
    print(so.maxProfit(a))
