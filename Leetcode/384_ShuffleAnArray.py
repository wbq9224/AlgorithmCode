from random import *


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.array = nums[:]

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.array

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        # 洗牌算法：循环i，每次生成一个i~n的随机数j，然后交换a[i]，a[j]
        # random有api shuffle可完成相同功能
        shuffle_array = self.array[:]
        for i in range(len(shuffle_array)):
            j = randint(i, len(shuffle_array) - 1)
            shuffle_array[i], shuffle_array[j] = shuffle_array[j], shuffle_array[i]

        return shuffle_array

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()