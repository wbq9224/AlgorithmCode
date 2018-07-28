class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        # 由于题目要求使用常数额外空间，以此只能考虑利用现有空间储存信息
        # 故可利用第0行和第0列存储相应的行和列是否要置0
        # 则原有的第0行和第0列的信息因为会丢失，故单独用两个标记先存出来其是否有0即可

        if not matrix:
            return

        m, n = len(matrix), len(matrix[0])

        # 单独标记首行首列是否有0
        first_row_have_zero = False
        first_col_have_zero = False
        for i in range(n):
            if matrix[0][i] == 0:
                first_row_have_zero = True
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_have_zero = True

        # 用首行首列去标记对应行和列是否有0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # 除首行首列外对其余部分置0
        for i in range(1, m):
            if matrix[i][0] == 0:
                matrix[i] = [0] * n
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0

        # 首行首列置0
        if first_row_have_zero:
            matrix[0] = [0] * n
        if first_col_have_zero:
            for i in range(m):
                matrix[i][0] = 0

        return


if __name__ == '__main__':
    # mat = [
    #   [1,1,1],
    #   [1,0,1],
    #   [1,1,1]
    # ]
    mat = [
      [0,1,2,0],
      [3,4,5,2],
      [1,3,1,5]
    ]

    Solution().setZeroes(mat)
    print(mat)
