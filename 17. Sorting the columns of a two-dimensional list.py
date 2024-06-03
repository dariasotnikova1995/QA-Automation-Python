matrix = [['a', 'c', 'e'],
          ['f', 'b', 'a'],
          ['a', 'n', 'k'],
          ['e', 'l', 'i']]
import numpy as np
num_cols = len(matrix[0])
transposed_matrix = []
for col in range(num_cols):
    column = []
    for row in range(len(matrix)):
        column.append(matrix[row][col])
    transposed_matrix.append(column)
for col in range(num_cols):
    transposed_matrix[col].sort()
result_matrix = []
for row in range(len(transposed_matrix[0])):
    new_row = []
    for col in range(num_cols):
        new_row.append(transposed_matrix[col][row])
    result_matrix.append(new_row)
print(np.array(result_matrix))