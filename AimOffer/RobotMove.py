# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.STEP_DIR = [[1,0], [0, 1], [-1, 0], [0, -1]]


    def get_value(self, x):
        temp_sum = 0
        while x:
            temp_sum += x % 10
            x = int(x / 10)
        return temp_sum


    def dfs(self, g, v, i, j, threshold, arrived):
        v[i][j] = True

        for each_step in self.STEP_DIR:
            temp_i = i + each_step[0]
            temp_j = j + each_step[1]
            if 0 <= temp_i < len(g) and 0 <= temp_j < len(g[0]) and not v[temp_i][temp_j] and g[temp_i][temp_j] <= threshold:
                arrived = self.dfs(g, v, temp_i, temp_j, threshold, arrived + 1)

        return arrived

    def movingCount(self, threshold, rows, cols):
        # write code here
        if threshold <= 0 or rows <= 0 or cols <= 0:
            return 0

        graph = []
        for i in range(rows):
            graph.append([])
            temp_rows = self.get_value(i)
            for j in range(cols):
                graph[-1].append(temp_rows + self.get_value(j))

        visited = [[False for j in range(cols)] for i in range(rows)]
        return self.dfs(graph, visited, 0, 0, threshold, 1)


if __name__ == '__main__':
    thre = 3
    r, c = 4, 4
    print(Solution().movingCount(thre, r, c))