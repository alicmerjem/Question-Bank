"""
write a function to calculate the
average value of the numbers in a 
given tuple of tuples
"""

def average_of_tuples(tup_of_tups):
    return [sum(tup) / len(tup) for tup in tup_of_tups]

# Test cases
print(average_of_tuples(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))))  # Output: [30.5, 34.25, 27.0, 23.25]
print(average_of_tuples(((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))))  # Output: [25.5, -18.0, 3.75]
