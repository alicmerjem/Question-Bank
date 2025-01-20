"""
return the centered average of an array
of ints, which well say is the mean 
average of the values, except ignoring
the largest and smallest values in the
arrays. if there are multiple copies of
the smallest value, ignore just one copy
and likewise for the largest value. use
int division to produce the final avg. 
you may assume that the array is 
length 3 or more
"""

def centered_avg(nums):
    nums.sort()
    return sum(nums[1:-1]) // (len(nums) - 2)