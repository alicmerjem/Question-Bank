"""
write a function to find the index of 
an item in a specified list
"""
def find_index(lst, item):
    if item in lst:
        return lst.index(item)
    else:
        return -1
    
sample = ['apple', 'banana', 'cherry']
print(find_index(sample, 'banana'))
print(find_index(sample, 'watermelon'))