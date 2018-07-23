def find_great(nums):
    if not nums:
        return -1

    # 方法一：不断保存加到大于0时的最大和，若小于零则舍弃
    max_sum, temp = -99999, 0
    for num in nums:
        if temp <= 0:
            temp = num
        else:
            temp += num
        max_sum = max(max_sum, temp)

    # 方法二：dp，状态转移方程f(i)= num[i] if i=0 or f(i-1)<0, f(i) = f(i-1) + num[i] if i !=0 or f(i-1)>0, 代码与上一致

    return max_sum


if __name__ == '__main__':
    num = [2, 8, 1, 5, 9]
    # num = [-2, -8, -1, -5, -9]
    # num = [1, -2, 3, 10, -4, 7, 2, -5]
    print(find_great(num))
