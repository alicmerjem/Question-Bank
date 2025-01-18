"""
total string length of all values
in a dictionary
"""

def total_len(dictionary):
    return sum(len(value) for value in dictionary.values())
