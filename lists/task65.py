"""
write a function to check if two given
lists contain the same elements 
regardless of order
"""

def same_elements(lst1, lst2):
    return sorted(lst1) == sorted(lst2)

print(same_elements([1, 2, 4], [4, 2, 1]))