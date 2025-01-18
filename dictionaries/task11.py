"""
create all combos of letters from
a dictionary
"""
def create_combos(data):
    keys = list(data.keys())
    for val1 in data[keys[0]]:
        for val2 in data[keys[1]]:
            print(val1 + val2)

data = {'1': ['a', 'b'], '2': ['c', 'd']}
create_combos(data)          