# 此题思路与归并排序基本一致，只不过要做修改的地方在于归并排序是采用从前到后合并两有序数组
# 而此处为了统计逆序数，需要从后向前合并


def merge(nums, temp_nums, left, mid, right):
    # 在原有归并排序的基础上做修改, 采用倒叙合并两有序子数组
    # 之所以倒叙合并是为了统计逆序数
    i, j, t = mid, right, right
    count = 0
    while i >= left and j >= mid + 1:
        if nums[i] > nums[j]:
            temp_nums[t] = nums[i]
            i -= 1
            count += j - mid  # 此句是关键，若当前两数字为逆序，则num[j]前的所有数与num[i]均构成逆序
        else:
            temp_nums[t] = nums[j]
            j -= 1
        t -= 1

    if i >= left:
        temp_nums[t - i + left: t + 1] = nums[left: i + 1]
    if j >= mid + 1:
        temp_nums[t - j + mid + 1: t + 1] = nums[mid + 1: j + 1]
    nums[left: right + 1] = temp_nums[left:right + 1]
    return count


def merge_sort_entry(nums, temp_nums, begin, end):
    if begin >= end:
        return 0

    mid = (begin + end) >> 1
    left_count = merge_sort_entry(nums, temp_nums, begin, mid)
    right_count = merge_sort_entry(nums, temp_nums, mid + 1, end)
    count = merge(nums, temp_nums, begin, mid, end)
    return count + left_count + right_count


def merge_sort(nums):
    if not nums:
        return
    temp = nums[:]
    count = merge_sort_entry(nums, temp, 0, len(nums) - 1)
    print(count)
    return


if __name__ == '__main__':
    number = [1, 2, 1, 2, 1]
    # number = [1, 2, 3, 4, 5, 6]
    # number = [6, 5, 4, 3, 2, 1]
    # number = [1, 2, 3, 4, 7, 6, 5]
    # number = [7, 5, 6, 4]
    # number = [9, 43, 12, 13, 1, 54, 20, 27, 2]
    merge_sort(number)

    print(number)