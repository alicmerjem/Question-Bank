"""
write a function to sum a specific 
column of a list in a given list
of lists
"""

def sum_col(nested_list, column_index):
    return sum(row[column_index] for row in nested_list)

nested_list = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
print(sum_col(nested_list, 0))
print(sum_col(nested_list, 1))
print(sum_col(nested_list, 3))