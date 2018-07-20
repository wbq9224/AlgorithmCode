import numpy as np


def find(mat, tar):
    if mat is None:
        return

    rows, cols = mat.shape
    row = 0
    col = cols - 1

    while row < rows and col >= 0:
        if mat[row][col] == tar:
            return 1, row, col
        elif matrix[row][col] > tar:
            col -= 1
        else:
            row += 1

    return 0, 0, 0


if __name__ == '__main__':
    matrix = np.array([
        [1, 2, 8, 9],
        [2, 4, 9, 12],
        [4, 7, 10, 13],
        [6, 8, 11, 15]
    ])
    rev = find(matrix, 20)
    print(rev)
    print(rev[0] > 0)
