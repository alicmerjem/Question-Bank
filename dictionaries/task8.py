"""
get max and min value in a dictionary
"""
def min_max(dict):
    return max(dict.values()), min(dict.values())

my_dict = {1: 10, 2: 20, 3: 30}
print(min_max(my_dict))