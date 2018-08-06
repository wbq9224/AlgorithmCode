class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """

        # 方法一：直接返回true，即alex必胜
        # 因为由于石子堆数为偶数，即0~n-1，则alex每次都可保证只取奇数位石子或只取偶数位石子
        # 例如，假设alex想只取偶数位石子，则alex第一次取第0个，则li只能去1或n-1中的一个，则留给alex的选择必为2或n-2此必为偶数位
        # 循环此过程即可保证alex只取到偶数位。反之亦然，只要alex第一次取n-1，则可保证其取到所有的奇数位石子
        # 故若所有偶数位石子的和大于所有奇数位石子之和，则alex取偶数位即可保证获胜
        # 若所有偶数位石子的和小于所有奇数位石子之和，则alex取奇数位即可保证获胜
        # 故alex是必胜的

        # return True

        # 方法二：动态规划
        # dp[i][j]表示从piles[i]~piles[j]中alex能取到的比li所取到的数中的最大值，每次只能取piles[i]或piles[j]
        # 若取piles[i]，则问题变为piles[i] - dp[i+1][j]
        # 若取piles[j]，则问题变为piles[j] - dp[i][j -1]
        # 故状态转移方程位dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j -1])

        n = len(piles)
        dp = [[0] * n for i in range(n)]
        for i in range(n):
            dp[i][i] = piles[i]
        for d in range(1, n):
            for i in range(n - d):
                dp[i][i + d] = max(piles[i] - dp[i + 1][i + d], piles[i + d] - dp[i][i + d - 1])
        print(dp)
        print(dp[0][-1])


if __name__ == '__main__':
    number = [3, 7, 2, 3]
    print(Solution().stoneGame(number))