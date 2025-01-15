"""
write a function to compute the sum of 
digits of a given string
"""

def function(s):
    total = 0

    for char in s:
        if char.isdigit():
            total += int(char)

    return total

print(function('123'))