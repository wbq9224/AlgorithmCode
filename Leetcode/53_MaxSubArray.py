class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        temp_sum, max_sum = nums[0], nums[0]
        for num in nums[1:]:
            if temp_sum < 0:
                temp_sum = num
            else:
                temp_sum += num
            max_sum = max(temp_sum, max_sum)
        return max_sum