# 求集合的幂集问题
# 将集合中的元素看作二进制位，则每一元素均有选中（1）或不选中（0）两种状态，递归求解
# 问题的规模为2**n


def dfs(index, s, bit, res):
    if index == len(s):
        temp = []
        for i in range(len(bit)):
            if bit[i] == 1:
                temp.append(s[i])
        res.append(temp)
        return
    bit[index] = 0
    dfs(index + 1, s, bit, res)
    bit[index] = 1
    dfs(index + 1, s, bit, res)
    return


if __name__ == '__main__':
    s = [i for i in range(26)]
    bit = [0 for i in range(len(s))]
    res = []
    dfs(0, s, bit, res)
    print(res)