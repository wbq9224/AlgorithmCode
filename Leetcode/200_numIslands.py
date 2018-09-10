class Solution(object):
    def __init__(self):
        self.DIRS = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def dfs(self, g, x, y, visited):
        visited[x][y] = True
        for dir in self.DIRS:
            temp_x = x + dir[0]
            temp_y = y + dir[1]
            if 0 <= temp_x < len(g) and 0 <= temp_y < len(g[0]) and not visited[temp_x][temp_y] and g[temp_x][
                temp_y] == "1":
                self.dfs(g, temp_x, temp_y, visited)
        return

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not visited[i][j]:
                    self.dfs(grid, i, j, visited)
                    count += 1

        return count