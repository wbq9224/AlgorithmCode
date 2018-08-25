class UnionFind:
    '''
        并查集：解决无向图连通性问题
    '''
    def __init__(self, n):
        # 每个结点的祖先
        self.s = [i for i in range(n)]
        # 每个结点所在树的秩
        self.r = [0 for i in range(n)]

    # 按秩合并：将秩小子树合并到秩大的子树中
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.r[rx] > self.r[ry]:
            self.s[ry] = rx  # 注意是将根进行合并，故为rx，ry进行操作
        else:
            if self.r[rx] == self.r[ry]:
                self.r[ry] += 1
            self.s[rx] = ry  # 注意是将根进行合并，故为rx，ry进行操作
        return

    # 路径压缩:在递归找到祖先后，回溯时将路径上所有结点都直接指向该祖先
    def find(self, x):
        if self.s[x] != x:
            self.s[x] = self.find(self.s[x])
        return self.s[x]


if __name__ == '__main__':
    u = UnionFind(15)
    u.union(0, 1)
    u.union(0, 7)
    u.union(3, 5)
    u.union(3, 6)
    u.union(4, 9)
    u.union(4, 10)
    u.union(5, 10)
    u.union(6, 8)
    u.union(6, 13)
    u.union(7, 8)
    u.union(8, 13)
    u.union(9, 11)
    u.union(9, 14)
    u.union(10, 11)

    res = 0
    for i in range(15):
        if u.find(i) == i:
            res += 1

    print(u.s)
    print(res)
