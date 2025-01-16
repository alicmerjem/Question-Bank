"""
write a python function to multiply
all itmes in a list
"""
def multiply_list(items):
    product = 1
    for item in items:
        product *= item 
    return product

numbers = [1, 2, 3, 4, 5]
print(multiply_list(numbers))