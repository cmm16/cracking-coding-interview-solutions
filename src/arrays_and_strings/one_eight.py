from collections import defaultdict


def zero_matrix(matrix):
    row_dict = defaultdict(bool)
    column_dict = defaultdict(bool)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                row_dict[i] = True
                column_dict[j] = True

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if row_dict[i]:
                matrix[i][j] = 0
            if column_dict[j]:
                matrix[i][j] = 0
