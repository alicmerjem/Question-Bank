"""
write a function to move all zero
digits to the end of a given list
of numbers
"""
def move_zeros(lst):
    non_zero = [x for x in lst if x!= 0]
    zeroes = [0] * (len(lst) - len(non_zero))
    return non_zero + zeroes 

sample = [3, 4, 0 ,0, 0, 0, 1]
print(move_zeros(sample))
