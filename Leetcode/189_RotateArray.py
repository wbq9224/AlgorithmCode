class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or k <= 0:
            return

        length = len(nums)

        # o(n)
        # copy = [num for num in nums]
        #
        # for i in range(length):
        #     index= (i + k) % length
        #     nums[index] = copy[i]

        # python切片是直接在原列表内存上进行的操作，因此满足题目条件
        # slice1:直接用切片做拼接
        # nums[:] = nums[length - k:] + nums[:length - k]

        # slice2:先对前n-k个逆序，再对后k个逆序，最终总体逆序
        # nums[:] = (nums[:length-k][::-1] + nums[length - k:][::-1])[::-1]

        return


if __name__ == '__main__':
    a = [1,2,3,4,5,6,7]
    k = 3

    so = Solution()
    so.rotate(a, k)
    print(a)