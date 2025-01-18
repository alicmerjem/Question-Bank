"""
write a function to extract a specified
column from a given nested list
"""
def extract_col(nested_list, column_index):
    return [row[column_index] for row in nested_list]

nested1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
print(extract_col(nested1, 0))