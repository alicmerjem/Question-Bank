"""
write a function to replace the last
element in a list with another list
"""

def replace_lasr(l1, l2):
    l1[-1:] = l2
    return l1

l1 = [1, 2, 3, 4, 5]
l2 = [2, 4, 6, 8]
print(replace_lasr(l1, l2))