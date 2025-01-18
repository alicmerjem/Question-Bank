"""
match key values in two dictionaries
"""
def match_key_values(d1, d2):
    for key in d1:
        if key in d2 and d1[key] == d2[key]:
            print('im too lazy to type')


d1 = {'key1': 1, 'key2': 3, 'key3': 2}
d2 = {'key1': 1, 'key2': 2}
match_key_values(d1, d2)