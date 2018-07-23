# 快速排序：不稳定，最好o（nlogn），最坏o（n**2），平均o（nlogn）
def qkpass(nums, left, right):
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


def qk_sort_entry(nums, begin, end):
    if begin > end:
        return

    mid = qkpass(nums, begin, end)
    qk_sort_entry(nums, begin, mid - 1)
    qk_sort_entry(nums, mid + 1, end)
    return


def qk_sort(nums):
    if nums is None:
        return

    qk_sort_entry(nums, 0, len(nums) - 1)
    return


# 冒泡排序：稳定，最好o(n), 最坏o（n ** 2）, 平均o（n ** 2）
def bubble_sort(nums):
    if nums is None:
        return
    length = len(nums)
    for i in range(length - 1, 0, -1):
        for j in range(1, i + 1):
            if nums[j - 1] > nums[j]:
                temp = nums[j - 1]
                nums[j - 1] = nums[j]
                nums[j] = temp
    return


# 选择排序：不稳定，最好最坏平均o（n ** 2）
def select_sort(nums):
    if nums is None:
        return
    length = len(nums)
    for i in range(length):
        k = i
        for j in range(i + 1, length):
            if nums[j] < nums[k]:
                k = j
        temp = nums[i]
        nums[i] = nums[k]
        nums[k] = temp
    return


# 堆排序：不稳定，最好最坏平均o（nlogn）
def sift(nums, begin, end):
    i = begin
    j = i * 2  # i的左孩子
    temp = nums[i]
    while j < end:
        if j < end and nums[j] < nums[j + 1]:  # 在i的左右孩子中选出较大者
            j += 1
        if nums[j] > temp:
            nums[i] = nums[j]  # 此处不用做交换，直接赋值相当于快排挖坑法
            i = j
            j = i * 2
        else:
            break
    nums[i] = temp  # 最后填坑
    return


def heap_sort(nums):
    if nums is None:
        return

    length = len(nums)
    for i in range(length >> 1, -1, -1):  # 从最后一个非叶节点开始倒序将所有子树调整为最大堆
        sift(nums, i, length - 1)

    for i in range(length - 1, 0, -1):
        temp = nums[0]  # 交换堆顶与堆底元素使选出的最大元素出堆
        nums[0] = nums[i]
        nums[i] = temp
        sift(nums, 0, i - 1)  # 因所有剩余子堆已是最大堆，因此只许调整新的堆顶使其为最大堆即可
    return


# 插入排序：稳定，最好o（n），最坏o（n ** 2），平均o（n ** 2）
def insert_sort(nums):
    if nums is None:
        return

    length = len(nums)
    for i in range(1, length):
        temp = nums[i]
        # 直接插入排序
        # j = i - 1
        # while j >= 0 and nums[j] > temp:
        #     nums[j + 1] = nums[j]
        #     j -= 1
        # nums[j + 1] = temp
        # 折半插入排序
        index = binary_search(nums[:i], temp)
        if index >= 0:
            j = i - 1
            while j >= index:
                nums[j + 1] = nums[j]
                j -= 1
            nums[index] = temp
    return


def binary_search(nums, target):
    if nums is None or len(nums) <= 0:
        return -1
    left = 0
    right = len(nums) - 1
    while left <= right:  # 注意此处一定是 <=
        mid = (left + right) >> 1
        if nums[mid] > target:  # 查找第一个大于target的数
            right = mid - 1
        else:
            left = mid + 1
    return left


#  最低位优先基数排序：稳定，平均最坏均为o（d（n+rd））（位数 *（元素个数+关键字取值范围））
def lsd(nums):
    if nums is None:
        return

    base = 1
    max_num = max(nums)  # 找出最大位数

    while max_num % 10 != 0:  # 控制当前应收集的数字位
        buskets = [[] for i in range(10)]  # 桶初始化

        for num in nums:  # 将数字按从当前位收集进相应的桶
            temp = int(num / base) % 10
            buskets[temp].append(num)

        nums[:] = [num for busket in buskets for num in busket]  # 将桶中数字分发

        base *= 10  # 进位
        max_num = int(max_num / 10)
    return


# 二路归并排序：稳定，最好最坏平均o（nlogn）
def merge(nums, temp, left, mid, right):  # 将两个有序子序列合并为一个有序序列
    i = left
    j = mid + 1
    t = 0
    while i <= mid and j <= right:
        if nums[i] < nums[j]:
            temp[t] = nums[i]
            i += 1
        else:
            temp[t] = nums[j]
            j += 1
        t += 1
    if i <= mid:
        temp[t: t + mid - i] = nums[i: mid + 1]
        t += mid - i
    if j <= right:
        temp[t: t + right - j] = nums[j: right + 1]
    nums[left:right + 1] = temp[:right - left + 1]


def merge_sort_entry(nums, temp, begin, end):
    if begin >= end:
        return

    mid = (begin + end) >> 1
    merge_sort_entry(nums, temp, begin, mid)
    merge_sort_entry(nums, temp, mid + 1, end)
    merge(nums, temp, begin, mid, end)
    return


def merge_sort(nums):
    if nums is None:
        return
    length = len(nums)
    nums_copy = nums[:]

    merge_sort_entry(nums, nums_copy, 0, length - 1)
    return


if __name__ == '__main__':
    # number = [0, 0, 0, 0, 0]
    number = [9, 43, 12, 13, 1, 54, 20, 27, 2]

    # qk_sort(number)
    # bubble_sort(number)
    # select_sort(number)
    # heap_sort(number)
    # insert_sort(number)
    # lsd(number)
    merge_sort(number)

    print(number)