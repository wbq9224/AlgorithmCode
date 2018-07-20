class Solution(object):

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 用到了异或的性质：
        # 1、n ^ 0 = n, n ^ n = 0
        # 2、a ^ b ^ c = a ^ c ^ b(交换律)
        # 因此对原数组依次做异或，则成对出现的数异或结果必为0，则最终异或结果即为只出现了一次的数

        length = len(nums)
        res = 0

        for i in range(length):
            res ^= nums[i]

        return res


if __name__ == '__main__':
    a = [4,1,2,1,2]
    so = Solution()
    print(so.singleNumber(a))
