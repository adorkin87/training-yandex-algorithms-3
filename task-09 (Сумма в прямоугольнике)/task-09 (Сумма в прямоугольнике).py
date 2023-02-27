with open('input.txt', 'r') as f:
    source_array = f.readlines()
n, m, k = map(int, source_array[0].split())
matrix = []
for i in range(1, n+1):
    matrix.append(list(map(int, source_array[i].split())))
pref_matrix = [[]]
for row in range(n):
    for col in range(m):
        if row == col == 0:
            pref_matrix[row].append(matrix[row][col])
        elif row == 0:
            pref_matrix[row].append(matrix[row][col] + pref_matrix[row][col - 1])
        elif col == 0:
            pref_matrix.append([])
            pref_matrix[row].append(matrix[row][col] + pref_matrix[row-1][col])
        else:
            pref_matrix[row].append(matrix[row][col]
                                    + pref_matrix[row][col - 1]
                                    + pref_matrix[row - 1][col]
                                    - pref_matrix[row - 1][col - 1])
for i in range(n+1, k+n+1):
    row_1, col_1, row_2, col_2 = map(int, source_array[i].split())
    if col_1 == row_1 == 1:
        result = pref_matrix[row_2-1][col_2-1]
    elif row_1 == 1:
        result = pref_matrix[row_2-1][col_2-1] - pref_matrix[row_2-1][col_1-1-1]
    elif col_1 == 1:
        result = pref_matrix[row_2-1][col_2-1] - pref_matrix[row_1-1-1][col_2-1]
    else:
        result = pref_matrix[row_2-1][col_2-1] \
                 - pref_matrix[row_2-1][col_1-1-1] \
                 - pref_matrix[row_1-1-1][col_2-1] \
                 + pref_matrix[row_1-1-1][col_1-1-1]
    print(result)
