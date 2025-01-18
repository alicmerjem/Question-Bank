"""
check if a key exists in a dictionary
"""

def check_key(dict, key):
    return key in dict

my_dict = {1: "a", 2: "b"}
print(check_key(my_dict, 2))