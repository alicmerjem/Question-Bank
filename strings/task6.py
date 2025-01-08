"""
write a function called removedup that
takes a string and creates a new string
by only adding those characters that 
are not already present. in other words,
there will never be a duplicate letter
added to the new string
"""

def removedup(s):
    result = ""
    for char in s:
        if char not in result:
            result += char
    return result