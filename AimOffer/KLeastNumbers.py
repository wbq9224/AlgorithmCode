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


def getLeastNumbers(nums, k):
    if not nums or k > len(nums) or k < 0:
        return

    index = partition(nums, 0, len(nums) - 1)
    while index != k - 1:
        if index > k - 1:
            index = partition(nums, 0, index - 1)
        else:
            index = partition(nums, index + 1, len(nums) - 1)
    return nums[:k]


if __name__ == '__main__':
    number = [4, 5, 1, 6, 2, 7, 3, 8]
    print(getLeastNumbers(number, 4))
