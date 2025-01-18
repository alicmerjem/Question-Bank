"""
remove spaces from dict keys
"""
def remove_spaces(dict):
    return {key.replace(' ', ''): value for key, value in dict.items()}

my_dict = {'key 1': 'value1', 'key 2': 'value2'}
print(remove_spaces(my_dict))