import numpy as np


# 挖坑法快速排序
def qkpass(arr, left, right):
    key = arr[right]
    while left < right:
        while left < right and arr[left] <= key:
            left += 1
        arr[right] = arr[left]
        while left < right and arr[right] >= key:
            right -= 1
        arr[left] = arr[right]
    arr[right] = key
    return right


def qksort(arr, begin, end):
    if begin >= end:
        return
    med = qkpass(arr, begin, end)
    qksort(arr, begin, med - 1)
    qksort(arr, med + 1, end)


def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if nums is None:
        return []

    length = len(nums)
    if length < 3:
        return []

    answer = []
    nums = sorted(nums)
    for i in range(length - 2):
        left = i + 1
        right = length - 1

        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        while left < right:
            res = nums[i] + nums[left] + nums[right]
            if res == 0:
                answer.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif res > 0:
                right -= 1
            else:
                left += 1

    return answer


def fourSum(nums, target):
    if nums is None:
        return []

    length = len(nums)
    if length < 4:
        return []
    elif length == 4 and sum(nums) == target:
        return [nums]

    answer = []
    nums = sorted(nums)
    for i in range(length - 3):
        if nums[i] > target and nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, length - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            left = j + 1
            right = length - 1
            while left < right:
                res = nums[i] + nums[j] + nums[left] + nums[right]
                if res == target:
                    answer.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif res > target:
                    right -= 1
                else:
                    left += 1
    return answer


def fourSumCount(A, B, C, D):
    if A is None or B is None or C is None or D is None:
        return 0
    dict = {}
    for a in A:
        for b in B:
            # a + b, 0表示若为Node则默认值为0否则取get(a+b)的value
            dict[a + b] = dict.get(a + b, 0) + 1
    res = 0
    for c in C:
        for d in D:
            temp = - c - d
            res += dict.get(temp, 0)

    return res

if __name__ == '__main__':
    # num_list = np.array([
    #     9, 43, 12, 13, 1, 54, 20, 27, 2
    # ])
    #
    # M = 30
    # res = 0
    #
    # qksort(num_list, 0, num_list.shape[0] - 1)
    #
    # # 从两端向中间进行遍历
    # for i, num in enumerate(num_list):
    #     left = i + 1
    #     right = num_list.shape[0] - 1
    #     # 转化为2 sum问题
    #     while left < right:
    #         if num + num_list[left] + num_list[right] < M:
    #             print(num, num_list[left], num_list[right])
    #             res += 1
    #             left += 1
    #         elif num + num_list[left] + num_list[right] >= M:
    #             right -= 1
    #
    # print(res)

    # # nums = [-1,0,1,2,-1,-4]
    # nums = [1,-2,-5,-4,-3,3,3,5]
    # # nums = [-3, -2, -1, 0, 0, 1, 2, 3]
    #
    # print(fourSum(nums, -11))

    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    print(fourSumCount(A, B, C, D))
