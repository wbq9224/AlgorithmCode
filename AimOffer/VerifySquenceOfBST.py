def verify(nums):
    if nums is None or len(nums) <= 0:
        return False

    length = len(nums)
    root = nums[length - 1]

    i = 0
    while i < length -1 and nums[i] < root:
        i += 1

    for j in range(i, length - 1):
        if nums[j] < root:
            return False

    left = right = True
    if i > 0:
        left = verify(nums[:i])
    if i < length - 1:
        right = verify(nums[i:length - 1])

    return left and right


if __name__ == '__main__':
    number = [4, 6, 12, 8, 16, 14, 10]

    print(verify(number))