"""
Question:
小摩有一个N个数的数组，他想将数组从小到大 排好序，但是萌萌的小摩只会下面这个操作：
任取数组中的一个数然后将它放置在数组的最后一个位置。
问最少操作多少次可以使得数组从小到大有序。
输入描述:
首先输入一个正整数N，接下来的一行输入N个整数。(N <= 50, 每个数的绝对值小于等于1000)
输出描述:
输出一行操作数
输入
4
19 7 8 25
输出
2
说明
19放到最后，25放到最后，两步完成从小到大排序
"""

import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    num = list(map(int, sys.stdin.readline().strip().split()))

    # 算法思想：统计原序列与排序后序列中拓扑顺序相同的元素个数，则其余元素均需移动
    sorted_num = sorted(num)
    i = j = count = 0
    while i < len(num):
        if num[i] == sorted_num[j]:
            j += 1
            count += 1
        i += 1
    print(len(num) - count)