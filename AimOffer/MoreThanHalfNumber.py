def partition(nums, left, right):
    key = nums[right]
    while left < right:
        while left < right and nums[left] <= key:
            left += 1
        nums[right] = nums[left]
        while left < right and nums[right] >= key:
            right -= 1
        nums[left] = nums[right]
    nums[right] = key
    return right


def solution_one(nums, begin, end):
    mid = (begin + end) >> 1

    index = partition(nums, begin, end)
    while index != mid:
        if index > mid:
            index = partition(nums, begin, index - 1)
        else:
            index = partition(nums, index + 1, end)

    res = nums[mid]
    if nums.count(res) < mid:
        return -1
    return res


def find(nums):
    if not nums:
        return -1

    # 方法一：利用快排的思想二分寻找中位数
    # res = solution_one(nums, 0, len(nums) - 1)

    # 方法二：由于出现次数超过数组长度一半的数字的出现次数比其余数字出现次数的总和还多，因此可利用这一特点
    # res, times = nums[0], 1
    # for i in range(1, len(nums)):
    #     if times == 0:
    #         times = 1
    #         res = nums[i]
    #     elif nums[i] == res:
    #         times += 1
    #     else:
    #         times -= 1
    #
    # 方法三：用hash
    d = {}
    for num in nums:
        d[num] = d.get(num, 0) + 1
    res = list(d.keys())[list(d.values()).index(max(d))]

    if nums.count(res) < (len(nums) >> 1):
        return -1
    return res


if __name__ == '__main__':
    exp = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    print(find(exp))