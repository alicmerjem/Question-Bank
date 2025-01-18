"""
write a function to calculate the sum
of the numbers in a list between the 
indices of a specified range
"""
def sum_in_rane(lst, start, end):
    return sum(lst[start:end + 1])

lst = [2, 1, 5, 4]
print(sum_in_rane(lst, 1, 2))
