class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        # 方法一：与最长子序列和一样的思路
        # max_profit = 0
        # dp = 0
        # for i in range(len(prices) - 1):
        #     if dp < 0:
        #         dp = prices[i + 1] - prices[i]
        #     else:
        #         dp += prices[i + 1] - prices[i]
        #     max_profit = max(max_profit, dp)

        # 方法二：记下截止到目前的最低价格，然后不断用每天价格减最低价格得到利润，取最大值
        max_profit = 0
        min_price = prices[0]
        for price in prices[1:]:
            if price < min_price:
                min_price = price
            max_profit = max(max_profit, price - min_price)

        return max_profit


if __name__ == '__main__':
    num = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(num))