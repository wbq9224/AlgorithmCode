class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None:
            return

        length = len(nums)
        if length < 2:
            return length

        p = 0
        q = 1
        while q < length:
            while q < length and nums[q] == nums[p]:
                q += 1
            if q < length:
                p += 1
                nums[p] = nums[q]

        return p + 1


if __name__ == '__main__':
    so = Solution()
    count = so.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
