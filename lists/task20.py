"""
write a function to get unique values
from a list
"""
def something(lst):
    return list(set(lst))

sample = [1, 1, 1, 2, 2, 3, 4]
print(something(sample))