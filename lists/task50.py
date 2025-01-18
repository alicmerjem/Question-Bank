"""
write a function to remove all elements
from a given list present in another 
list
"""

def removing_something(l1, l2):
    return [item for item in l1 if item not in l2]

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = [2, 4, 6, 8]

print(removing_something(l1, l2))