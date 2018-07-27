class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # 也可不用辅助数组dp，只用3个变量保存前天，昨天和今天的最优值，然后不断交换即可
        dp = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            dp.append(max(dp[i - 1], dp[i - 2] + nums[i]))

        return dp[-1]


if __name__ == '__main__':
    number = [2,7,9,3,1]
    Solution().rob(number)