"""
write a function to remove a specified 
column from a given nested list
"""

def remove_col(nested_list, column_index):
    return [row[:column_index] + row[column_index + 1:] for row in nested_list]

nested = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
print(remove_col(nested, 0))