"""
Write a function that, for a 
given dictionary (whose all 
values are integers), 
returns a dictionary in which 
all values smaller than 9 are doubled.
"""

def double_values_below_9(d):
    return {key: value * 2 if value < 9 else value for key, value in d.items()}

# Example usage:
mydict = {"a": 5, "b": 8, "c": 10}
print(double_values_below_9(mydict))
