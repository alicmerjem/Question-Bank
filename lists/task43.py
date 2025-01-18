"""
write a function to find the difference
between consecutive numbers in a given
list
"""
def find_difference(nums):
    return [nums[i] - nums[i-1] for i in range(1, len(nums))]

nums = [1, 1, 3, 4, 4, 5, 6, 7]
print(find_difference(nums))