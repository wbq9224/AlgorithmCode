# 将分割标准定义为函数，可提高程序的可扩展性
def reorder(arr, fun):
    if arr is None or len(arr) == 0 or type(fun(arr[0])) is not bool:
        return

    left = 0
    right = len(arr) - 1
    while left < right:
        while left < right and fun(arr[left]):
            left += 1
        while left < right and not fun(arr[right]):
            right -= 1
        if left < right:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp

    return arr


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    print(reorder(a, lambda x: x & 1 == 1))