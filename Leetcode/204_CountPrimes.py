class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 朴素算法时间复杂度过高
        # 因此采用埃拉托斯特尼筛选法, 即使用标记数组，从2开始到√n结束，将每一个当前为正的数（即质数）其到n之间的所有倍数全部标记为负。

        if n <= 1:
            return 0

        flag = [True] * n
        for i in range(2, int(n ** 0.5) + 1):  # 从2开始到√n
            if flag[i]:
                for j in range(i * i, n, i):  # 注意此处， 可从i*i开始，因为小于i*i的必已被之前标记过了
                    flag[j] = False

        return flag.count(True) - 2  # 减去0和1这两个非质数


if __name__ == '__main__':
    print(Solution().countPrimes(10))