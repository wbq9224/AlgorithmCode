# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.STEP_DIR = [[-1, 0], [0, -1], [0, 1], [1, 0]]

    # 经典回溯法
    def dfs(self, g, f, i, j, index, path):
        # 标记当前状态
        f[i][j] = False

        # 终止条件
        if index == len(path) - 1:
            return True
        elif index < len(path) - 1:
            # 在当前状态可到达的子状态集中搜索
            for each_step in self.STEP_DIR:
                temp_i = i + each_step[0]
                temp_j = j + each_step[1]
                # 若下一步状态合法，则将当前状态转移至下一步状态
                if 0 <= temp_i < len(g) and 0 <= temp_j < len(g[0]) and f[temp_i][temp_j] and path[index + 1] == \
                        g[temp_i][temp_j]:
                    # 状态返回
                    if self.dfs(g, f, temp_i, temp_j, index + 1, path):
                        return True

        # 若失败，状态回溯
        f[i][j] = True
        return False

    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if not matrix or rows <= 0 or cols <= 0 or rows * cols != len(matrix) or len(path) > len(matrix):
            return False
        graph = [[matrix[(i - 1) * cols + j] for j in range(cols)] for i in range(1, rows + 1)]
        flag = [[True for j in range(cols)] for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if graph[i][j] == path[0] and self.dfs(graph, flag, i, j, 0, path):
                    return True
        return False


if __name__ == '__main__':
    mat = "abcesfcsadee"
    rows, cols = 3, 4
    path = "bcced"
    print(Solution().hasPath(mat, rows, cols, path))