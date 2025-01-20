"""
return the number of even ints in the
given array. 
note - the % mod operator computes the 
remainder, e.g. 5 % 2 is 1
"""
def counting_even(nums):
    return sum(1 for num in nums if num % 2 == 0)
