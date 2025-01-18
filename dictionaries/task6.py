"""
multiply all values in a dictionary
"""

def multiply_values(dict):
    result = 1
    for value in dict.values():
        result *= value
    return result

my_dict = {1: 10, 2: 20, 3: 30}
print(multiply_values(my_dict))