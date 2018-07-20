import numpy as np


def min(arr):
    if arr is None or len(arr) <= 0:
        return

    # 旋转后数组在查找时可利用二分查找
    mid = left = 0
    right = len(arr) - 1

    while arr[left] >= arr[right]:
        if right - left == 1:
            mid = right
            break

        mid = int((left + right) / 2)
        if arr[left] == arr[mid] and arr[left] == arr[right]:  # 处理有多个相同数字的情况，此时无法使用二分法，只能通过顺序遍历进行查找
            min_index = left
            for i in range(left, right + 1):
                if arr[i] < arr[min_index]:
                    min_index = i
            mid = min_index
            break

        # 一般情况，用二分法进行查找
        if arr[mid] >= arr[left]:
            left = mid
        elif arr[mid] <= arr[right]:
            right = mid

    return arr[mid]


if __name__ == '__main__':
    a = np.array([
        1, 2, 2, 2, 0, 1
    ])

    print(min(a))
