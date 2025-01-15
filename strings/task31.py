"""
write a function to find the first
repeated character in a given string
"""

def function(s):
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return None

print(function('swiss'))
print(function('racecar'))
print(function('abcdef'))