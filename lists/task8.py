"""
write a function to clone or copy a list
"""
def clone_copy(lst):
    # return lst.copy()
    return lst[:]

original = [1, 2, 3, 4, 5]
cloned = clone_copy(original)
print(cloned)