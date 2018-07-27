# 判断条件和返回值应如何理解：
# 按待寻找条件会将数组分为左右部分，如下面的找最后一个小于k的数字位置，则会将数组分为左：小于k，右：大于等于k两部分
# 则循环结束后left必指向右的第一个，right指向左的最后一个，按需返回即可


def find_first_K(nums, k):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) >> 1
        if nums[mid] >= k:  # 找到最后一个小于k的数字位置
            right = mid - 1
        else:
            left = mid + 1
    return right + 1  # 返回最后一个小于k的数字位置+1即第一个k的位置


def find_last_K(nums, k):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) >> 1
        if nums[mid] > k:  # 找到第一个大于k的数字位置
            right = mid - 1
        else:
            left = mid + 1
    return left - 1  # 返回第一个大于k的数字位置-1即最后一个k的位置


if __name__ == '__main__':
    number = [1, 2, 3, 3, 3, 3, 4, 5]
    k = 4

    print(find_last_K(number, k) - find_first_K(number, k) + 1)


