"""
write a function that computes the sum
of all elements in a list up to but not
including the first number bigger than 5
"""
def some_up_to_5(nums):
    total = 0
    for num in nums:
        if num > 5:
            break
        total+= num
    return total