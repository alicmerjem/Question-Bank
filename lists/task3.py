"""
write a python function to get the 
largest number from a list
"""
def largest_num(items):
    largest = items[0]
    for item in items:
        if item > largest:
            largest = item
    return largest

numbers = [1, 2, 3, 4, 5]
print(largest_num(numbers))