class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if board is None or len(board) != 9:
            return False
        for row in board:
            if len(row) != 9:
                return False

        # 方法一：直观思路：行、列、块分别检查
        # for row in board:
        #     digit_in_row = list(filter(lambda x: x != ".", row))
        #     if len(digit_in_row) != len(set(digit_in_row)):
        #         return False
        #
        # for col in range(9):
        #     digit_in_col = list(filter(lambda x: x != ".", [row[col] for row in board]))
        #     if len(digit_in_col) != len(set(digit_in_col)):
        #         return False
        #
        # for block_row in range(0, 9, 3):
        #     block_in_row = board[block_row:block_row + 3]
        #     for block_col in range(0, 9, 3):
        #         block = list(filter(lambda x: x != ".", [row[col] for row in block_in_row for col in range(block_col, block_col + 3)]))
        #         if len(block) != len(set(block)):
        #             return False

        # 方法二：空间换时间
        row = [[False for i in range(9)] for j in range(9)]
        col = [[False for i in range(9)] for j in range(9)]
        block = [[False for i in range(9)] for j in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    digit_index = int(board[i][j]) - 1
                    # 每行最多三个九宫格，3*(i/3)表示在这一行上九宫格开始的索引，j/3代表列偏移量，故整体索引为3*(i/3)+(j/3)
                    if row[i][digit_index] or col[j][digit_index] or block[i - i % 3 + int(j / 3)][digit_index]:
                        return False
                    row[i][digit_index] = col[j][digit_index] = block[3 * int(i / 3) + int(j / 3)][digit_index] = True
        return True


if __name__ == '__main__':
    # board_ex = [
    #   ["5","3",".",".","7",".",".",".","."],
    #   ["6",".",".","1","9","5",".",".","."],
    #   [".","9","8",".",".",".",".","6","."],
    #   ["8",".",".",".","6",".",".",".","3"],
    #   ["4",".",".","8",".","3",".",".","1"],
    #   ["7",".",".",".","2",".",".",".","6"],
    #   [".","6",".",".",".",".","2","8","."],
    #   [".",".",".","4","1","9",".",".","5"],
    #   [".",".",".",".","8",".",".","7","9"]
    # ]
    board_ex = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    print(Solution().isValidSudoku(board_ex))

