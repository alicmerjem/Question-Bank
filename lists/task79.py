"""
given an array length 1 or more of ints,
return the idfference between the largest
and smallest values in the array. 
note - the built in min(v1, v2) and
max(v1, v2) functions return the 
smallest or larger of two vales
"""
def difference(nums):
    return max(nums) - min(nums)