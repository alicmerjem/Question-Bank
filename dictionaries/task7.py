"""
remove a key from a dictionary
"""
def remove_key(dict, key):
    dict.pop(key, None)
    return dict

my_dict = {1: "a", 2: "b", 3: "c"}
print(remove_key(my_dict, 2))