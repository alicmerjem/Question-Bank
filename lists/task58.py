"""
write a function to get the index of the
first element which is greater than a 
specified element
"""

def first_index_greater(lst, value):
    for i, num in enumerate(lst):
        if num > value:
            return i
    return -1

lst = [12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83]
print(first_index_greater(lst, 73))
print(first_index_greater(lst, 21))
print(first_index_greater(lst, 80))
print(first_index_greater(lst, 55))