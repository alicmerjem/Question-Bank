"""
Write a function that for given 3 int 
values a b and c returns their sum.
If one of the values is the same as 
another of the values, it does not count
towards the sum.
"""
def loneSum(a, b, c):
    nums = [a, b, c]
    nums = [num for num in nums if nums.count(num)==1]
    return sum(nums)

print(loneSum(1, 2, 3))
print(loneSum(3, 2, 3))
print(loneSum(3, 3, 3))