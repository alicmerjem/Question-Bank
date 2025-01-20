"""
given an array of ints, return the sum
of the first 2 elements in the array
if the array is length less than 2, 
just sum up the elements that exist,
returning 0 if the array length is 0
"""

def first_two(numbers):
    return sum(numbers[:2])
