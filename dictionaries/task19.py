"""
find the key of a max value in a 
dictionary
"""

def find_max(dict):
    max_val = max(dict.values())
    max_key = max(key for key, value in dict.items() if value == max_val)

    return max_key[0], max_val
