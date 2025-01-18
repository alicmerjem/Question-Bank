"""
Write a function that, for a given 
dictionary (whose all values 
are integers), returns a dictionary
in which all values are replaced by
their rightmost digit.
"""

def replace_rightmost(d):
    return {key: value % 10 for key, value in d.items()}
