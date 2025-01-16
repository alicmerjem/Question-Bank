"""
write a function to remove duplicates
from a list
"""
def remove_duplicates(items):
    unique = []
    for item in items:
        if item not in unique:
            unique.append(item)
    return unique

numbers = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(numbers))