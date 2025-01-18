"""
sum of all values in a dictionary
"""

def sum_values(dict):
    return sum(dict.values())


my_dict = {1: 10, 2: 20, 3: 30}
print(sum_values(my_dict))