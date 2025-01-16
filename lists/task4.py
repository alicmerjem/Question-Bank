"""
write a function to get the smallest
number from a list
"""
def smallest_num(items):
    smallest = items[0]
    for item in items:
        if item < smallest:
            smallest = item
    return smallest


numbers = [1, 2, 3, 4, 5]
print(smallest_num(numbers))