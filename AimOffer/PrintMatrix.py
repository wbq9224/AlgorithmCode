def print_matrix(matrix):
    if matrix is None or len(matrix) <= 0 or len(matrix[0]) <= 0:
        return

    row = len(matrix)
    col = len(matrix[0])

    if row == 1 and col == 1:
        print(matrix[row - 1][col - 1])
        return
    if row == 1:
        for num in matrix[0]:
            print(num, end=' ')
        return
    if col == 1:
        for r in matrix:
            print(r[0], end=' ')
        return

    for num in matrix[0]:
        print(num, end=' ')
    for i in range(1, row):
        print(matrix[i][col - 1], end=' ')
    for i in range(col - 2, -1, -1):
        print(matrix[row - 1][i], end=' ')
    for i in range(row - 2, 0, -1):
        print(matrix[i][0], end=' ')

    new_matrix = matrix[1:row - 1]
    for row in new_matrix:
        row[:] = row[1: col - 1]

    print_matrix(new_matrix)


if __name__ == '__main__':
    l = []
    # l = [[1, 4, 7, 10]]
    # l = [[1], [4], [7], [10]]
    # l = [[1, 2], [4, 5], [7, 8], [10, 11]]
    # l = [[1, 2, 3, 4, 5], [4, 5, 6, 7, 8], [7, 8, 9, 10, 11], [10, 11, 12, 13, 14]]
    # l = [[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10], [10, 11, 12, 13]]
    print_matrix(l)