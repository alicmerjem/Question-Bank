"""
write a python function to sum all
items in a list
"""
def sum_list(items):
    total = 0
    for item in items:
        total+= item
    return total


numbers = [1, 2, 4, 5, 6]
print(sum_list(numbers))