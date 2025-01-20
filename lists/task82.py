"""
Return the sum of the numbers in the
array, except ignore sections of 
numbers starting with a 6 and 
extending to the next 7 
(every 6 will be followed by at least 
one 7). Return 0 for no numbers.
"""

def something(nums):
    total = 0
    in_section = False
    for num in nums:
        if num == 6:
            in_section = True
        elif num == 7 and in_section:
            in_section = False
        elif not in_section:
            total += num
    return total
