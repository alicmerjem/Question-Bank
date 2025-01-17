"""
write a function to find the list in a
list of lists whose sum of elements is
the highest
"""

def list_highest_sum(lst):
    return max(lists, key = sum)

lists = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
print(list_highest_sum(lists))