class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # 方法一：用库函数加字符串拼接补0再直接对字符串反序
        # binary = bin(n)[2:]
        # return int(((32 - len(binary)) * '0' + str(binary))[::-1], 2)

        # 方法二：以res代表新数，每次取原数末位数放在res后让res左移，原数右移更新末尾数字即可
        res = 0
        for i in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        return res


if __name__ == '__main__':
    print(Solution().reverseBits(43261596))