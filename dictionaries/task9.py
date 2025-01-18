"""
combine two dictionaries by adding 
values for common keys
"""
def combine_dicts(d1, d2):
    result = d1.copy()
    for key, value in d2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
print(combine_dicts(d1, d2))