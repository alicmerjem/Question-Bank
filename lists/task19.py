"""
write a function to find the second 
largest number in a list
"""
def second_largest(lst):
    sortedl = sorted(lst, reverse = True)
    return sortedl[1] if len(sortedl) > 1 else None

list = [1, 4, 6, 2]
print(second_largest(list))
