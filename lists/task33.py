"""
write a function to find all values in
a list that are greater than a specified
number
"""
def values_greater(lst, num):
    return [x for x in lst if x>num]

sample = [1, 2, 3, 4, 5]
num = 3
print(values_greater(sample, num))