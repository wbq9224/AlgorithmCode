# 在排序数列中找到和为key的两个数
def two_sum(nums, key):
    if not nums:
        return -1

    left, right = 0, len(nums) - 1
    while left < right:
        temp = nums[left] + nums[right]
        if temp == key:
            return nums[left], nums[right]
        elif temp > key:
            right -= 1
        else:
            left += 1

    return -1


# 和为key的连续正数序列
def continue_squence_sum(key):
    nums = [num for num in range(1, key)]

    left = 0
    right = 1
    while left < (key + 1) >> 1:  # 因数列之和至少要2个数，则k/2 + k/2 + 1必大于等于k，因此循环至（k+1）/2即可
        if sum(nums[left: right + 1]) < key:
            right += 1
        elif sum(nums[left: right + 1]) > key:
            left += 1
        else:
            print(nums[left: right + 1])
            right += 1
    return


if __name__ == '__main__':
    number = [1, 2, 4, 7, 11, 15]
    key = 20

    # print(two_sum(number, key))

    continue_squence_sum(15)
