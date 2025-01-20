"""
given an arrat of ints, return true if
6 appears as either the first or last
element in the array. the array will
be length 1 or more
"""

def first_last6(nums):
    return nums[0] == 6 or nums[-1] == 6