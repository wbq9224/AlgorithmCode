class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None:
            return

        length = len(nums)

        i = -1
        zero_count = 0
        while i < length:
            i += 1
            if nums[i] == 0:
                nums.append(nums.pop(i))
                i -= 1
                zero_count += 1
            if i >= length - zero_count - 1:
                break


if __name__ == '__main__':
    # num = [1, 2, 3, 4, 5]
    num = [0, 1, 0, 3, 12]
    Solution().moveZeroes(num)
    print(num)