"""
write a function to check if a list is 
empty or not
"""
def is_empty(lst):
    return len(lst) == 0

test1 = []
print(is_empty(test1))

test2 = [1, 2]
print(is_empty(test2))