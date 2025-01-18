"""
write a function to compute the average
of two given lists
"""

def find_average(l1, l2):
    combined = l1 + l2
    return sum(combined) / len(combined)

l1 = [1, 1, 3, 4, 4, 5, 6, 7]
l2 = [0, 1, 2, 3, 4, 4, 5, 7, 8]
print(find_average(l1, l2)) 