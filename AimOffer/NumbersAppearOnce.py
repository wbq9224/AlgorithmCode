def find(nums):
    if not nums or len(nums) <= 1:
        return

    # 通过异或找到两独立数字的异或结果，则此结果的二进制中至少为一位为1（异或的性质）
    exclusive_or = 0
    for num in nums:
        exclusive_or ^= num

    # 找到第一个1这一位的位置
    bit_index = 0
    while exclusive_or & 1 != 1:
        exclusive_or = exclusive_or >> 1
        bit_index += 1

    # 依据此位是否为1可将原数组分为2部分，且相同数字必在同一部分，而不同的两数必分在两边
    nums1 = []
    nums2 = []
    for num in nums:
        if (num >> bit_index) & 1 == 0:
            nums1.append(num)
        else:
            nums2.append(num)

    # 再用异或在子数组中分别统计即可
    res1, res2 = 0, 0
    for num in nums1:
        res1 ^= num
    for num in nums2:
        res2 ^= num

    return res1, res2


if __name__ == '__main__':
    number = [2, 4, 3, 6, 3, 2, 5, 5]
    print(find(number))