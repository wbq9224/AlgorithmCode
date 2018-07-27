def dp(n):
    if not n:
        return

    # 初始状态：
    # 只保留上层状态dp1和本层状态dp2，因此只需两个一维数组即可，无需二维数组，空间消耗过大
    # n个骰子可能出现的和有6n个，加1是让数组的0下标空出来，故数组长度为6n+1，让数组从1~n保存信息而不是0~n-1，故下面所有range函数均要加1
    dp1 = [0] * (6 * n + 1)
    for i in range(1, 7):
        dp1[i] = 1

    # 状态转移：
    # i表示骰子的总个数，故为从2到n
    # j表示有i个骰子时可能出现的和，故其最小为i，最大为6i
    # 当我有i-1个骰子时，再增加一个骰子，这个骰子的点数只可能为1、2、3、4、5或6,记为k。那i个骰子得到点数和为j的情况有：
    # (i-1,j-1)：第k个骰子投了点数1，(i-1,j-2)：第k个骰子投了点数2，.... ，(i-1,j-6)：第k个骰子投了点数6
    # 在i-1个骰子的基础上，再增加一个骰子出现点数和为j的结果只有这6种情况
    # 所以：f(i,j)=f(i-1,j-1)+f(i-1,j-2)+f(i-1,j-3)+f(i-1,j-4)+f(i-1,j-5)+f(i-1,j-6)
    for i in range(2, n + 1):
        dp2 = [0] * (6 * n + 1)
        for j in range(i, 6 * i + 1):
            for k in range(1, 7):
                dp2[j] += dp1[j - k] if j > k else 0
        dp1 = dp2

    print(dp1)
    total_count = 6 ** n
    probabilty = [i / total_count for i in dp1]
    print(probabilty)


if __name__ == '__main__':
    n = 3
    dp(n)