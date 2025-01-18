"""
write a python function to sort a 
given matrix in ascending order 
according to the sum of its rows
"""

def sort_matrix(matrix):
    return sorted(matrix, key = sum)

matrix = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
print(sort_matrix(matrix))