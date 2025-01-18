"""
iterate over dictionaries using for
loop
"""

def iterate_dict(dictionary):
    for key, value in dictionary.items():
        print('Key: ', key, "value: ", value)

my_dict = {1: "a", 2: "b", 3: "c"}
iterate_dict(my_dict)    