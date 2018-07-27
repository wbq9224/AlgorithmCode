class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        n = len(nums)
        return (n * (n + 1) >> 1) - sum(nums)


if __name__ == '__main__':
    print(Solution().missingNumber([9,6,4,2,3,5,7,0,1]))