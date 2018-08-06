import sys


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 使用m1, m2两个变量，若m1被更新则说明存在单个更小的值，若m2被更新，则说明在先前的m1的基础上存在一个递增元素，且不断将m2更新为最接近m1的值
        # 若能满足大于m2，则说明必存在一个递增的三元素序列

        if not nums:
            return False

        m1, m2 = sys.maxsize, sys.maxsize
        for num in nums:
            if num <= m1:
                m1 = num
            elif num <= m2:
                m2 = num
            else:
                return True

        return False


if __name__ == '__main__':
    number = [3, 5, 4, 7, 8]
    Solution().increasingTriplet(number)