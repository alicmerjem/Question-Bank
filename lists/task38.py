"""
write a python function to insert an
element at a specified position into
a given list
"""
def insert_at(lst, element, k):
    lst.insert(k, element)
    return lst

sample = [1, 1, 2, 3, 4, 4, 5, 1]
element = 22
k = 2
print(insert_at(sample, element, k))