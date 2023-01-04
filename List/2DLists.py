
# A 2D list is a matrix formation
# [
#     1 2 3
#     4 5 6
#     7 8 9
# ]
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print('*' * 6, 'new concept', '*' * 6)
print(matrix)
matrix[0][1]
print('*' * 6, 'new concept', '*' * 6)
print(matrix[0][1])
print('*' * 6, 'new concept', '*' * 6)

# Looping through the matrix
for row in matrix:
    # print(row)
    for item in row:
        print(item)
