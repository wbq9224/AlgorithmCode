# http://acm.fzu.edu.cn/problem.php?pid=2163
# 多米诺骨牌问题：单调栈
# 单调栈应用：https://blog.csdn.net/wubaizhe/article/details/70136174

while 1:
    n = input()
    if n != "":
        n = int(n)
        maps = []
        for i in range(n):
            x, h = map(int, input().split())
            maps.append([i, x, h])

        maps = sorted(maps, key=lambda temp: temp[1])

        stack, res = [], [0 for i in range(n)]
        for i in range(n):
            temp = [maps[i][0], i, maps[i][1] + maps[i][2] - 1]
            while stack and stack[-1][2] < maps[i][1]:
                tmp = stack.pop()
                res[tmp[0]] = i - tmp[1]
            stack.append(temp)
        while stack:
            tmp = stack.pop()
            res[tmp[0]] = n - tmp[1]
        print(res)
    else:
        break



