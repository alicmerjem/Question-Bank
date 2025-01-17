"""
write a function to check whether the 
nth element exists in a given list
"""
def check_exists(lst, n):
    return n < len(lst)

sample = [1, 2, 3, 4, 5]
print(check_exists(sample))