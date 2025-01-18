"""
Write a function that, for a 
given dictionary (whose all
values are integers), returns a 
dictionary in which all values 
smaller than 14 are doubled.
"""

def doubled_below(d):
    return {key: value * 2 if value < 14 else value for value, key in d.items()}