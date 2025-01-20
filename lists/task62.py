"""
write a function to find the indices of
elements of a given list, greater than
a specified value
"""
def indices_greater_than(lst, value):
    indices = []
    for i in range(len(lst)):
        if lst[i] > value:
            indices.append(i)
    return indices

print(indices_greater_than([1234, 1522, 1984, 19372, 1000, 2342, 7626], 3000))  # [3, 6]
print(indices_greater_than([1234, 1522, 1984, 19372, 1000, 2342, 7626], 20000))  # []