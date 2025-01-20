"""
given an array of ints length 3, figure
out which is larger, the first or last
element in the aray, and set all the 
other elements to be that value
return the changed array
"""

def max_end(nums):
    max_val = max(nums[0], nums[-1])
    return [max_val, max_val, max_val]