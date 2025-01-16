"""
write a function to get the difference
between 2 lists
"""
def difference_lst(l1, l2):
    return list(set(l1) - set(l2))

l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]
print(difference_lst(l1, l2))