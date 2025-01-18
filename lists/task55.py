"""
write a function to remove empty lists
from a given list of lists
"""

def remove_empty(lst):
    return [item for item in lst if item]

lst = [[], [], 'python', 2, '2 is a string', [], 'man i love the color blue']
print(remove_empty(lst))