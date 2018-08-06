class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if not grid:
            return 0

        v = 0
        v += sum([1 if grid[i][j] else 0 for i in range(len(grid)) for j in range(len(grid[i]))])
        v += sum(map(max, grid))
        v += sum(map(max, zip(*grid)))

        return v


if __name__ == '__main__':
    gr = [[1, 0],[0, 2]]
    # gr = [[1, 2], [3, 4]]
    print(Solution().projectionArea(gr))