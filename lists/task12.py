"""
write a function to print the numbers
of a specified list after removing even
numbers from it
"""
def remove_even(lst):
    return [num for num in lst if num % 2 != 0]

sample = [1, 2, 3, 4, 5, 6, 7, 8]
print(remove_even(sample))