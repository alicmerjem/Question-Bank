"""
write a function to find the item
with max occurences in a given list
"""

def find_max(nums):
    return max(set(nums), key=nums.count)

nums = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
print(find_max(nums))