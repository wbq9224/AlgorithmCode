def josephuse(n, m):
    if not n or not m:
        return -1

    # 动态规划法：
    # 第一个出列的人的位置必为(m-1)%n, 记为k
    # 则剩余序列为k+1, k+2,...,n-1,0,1,2,...,k-1
    # 将上述序列映射为0,1,2,...,n-2，则映射公式为(x-(k+1))%n, 则逆映射为(x+k+1)%n，带入k有(x+m)%n
    # 则经过映射后的问题完全变成了一个(n-1, m)的约瑟夫环子问题，最终n=1时出列的必为第0人
    # 故递推公式为：f(n,m)=(f(n-1,m)+m)%n, n=0时f(0,m)=0自底向上递推即可

    # 边界
    dp = 0

    for i in range(2, n + 1):
        dp = (dp + m) % i

    return dp


if __name__ == '__main__':
    print(josephuse(0, 0))