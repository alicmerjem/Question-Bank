"""
write a function to lowercase first 
in characters in a given string
"""

def function(s, n):
    return s[:n].lower() + s[n:]

print(function('W3RESOURCE.COM', 4))