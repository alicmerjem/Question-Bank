"""
write a function to find the second
smallest number in a list
"""
def second_smallest(lst):
    sortedl = sorted(lst)
    return sortedl[1] if len(sortedl) > 1 else None

list = [7, 3, 2, 15, 4]
print(second_smallest(list))