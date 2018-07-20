class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None:
            return

        length = len(nums)

        # 方法一：利用python list特性，遇0出队再加入队尾，时间复杂度为O（n * （pop + append））
        # i = -1
        # zero_count = 0
        # while i < length:
        #     i += 1
        #     if nums[i] == 0:
        #         nums.append(nums.pop(i))
        #         i -= 1
        #         zero_count += 1
        #     if i >= length - zero_count - 1:
        #         break

        # 方法二：利用尾部两个指针，其中last始终指向尾部待插入0的位置，current向前探测，若current遇0则将last-current中元素全部前移，
        # 再将0插入last指向的位置后last再前移。效率不高因为每个非0元素相当于移动了多次。
        # last = current = length - 1
        # while current >= 0:
        #     if nums[current] == 0:
        #         for i in range(last - current):
        #             nums[current + i] = nums[current + i + 1]
        #         nums[last] = 0
        #         last -= 1
        #     current -= 1

        # 方法三：利用zero_index指针始终指向当前未被处理的0的位置，一旦遇到非0元素即将其复制到zero_index所指向位置后移动zero_index到
        # 下一个0元素位置。时间复杂度O(n)
        zero_index = 0
        for i in range(length):
            if nums[i] != 0:
                nums[zero_index] = nums[i]
                zero_index += 1
        nums[zero_index:] = [0 for i in range(length - zero_index)]

        return

if __name__ == '__main__':
    # num = [0, 0, 0, 0, 0]
    # num = [1, 2, 3, 4, 5]
    num = [0, 1, 0, 3, 12]
    Solution().moveZeroes(num)
    print(num)