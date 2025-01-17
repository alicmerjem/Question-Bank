"""
write a function to count the number
of lists in a given list of lists
"""

def count_lists_in_list_of_lists(lst_of_lists):
    return len([x for x in lst_of_lists if isinstance(x, list)])

# Example usage
list_of_lists1 = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
list_of_lists2 = [[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]
print(count_lists_in_list_of_lists(list_of_lists1))  # 4
print(count_lists_in_list_of_lists(list_of_lists2))  # 3
