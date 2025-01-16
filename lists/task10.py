"""
write a python function that takes
two lists and returns true if they have 
at least one common member
"""

def common(l1, l2):
    for item in l1:
        if item in l2:
            return True
    return False

l1 = [1, 2, 3, 4, 5]
l2 = [5, 6, 7, 8, 9]
print(common(l1, l2))