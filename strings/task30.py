"""
write a function to find the first
non repeating characters in a given
string
"""

def function(s):
    for char in s:
        if s.count(char) == 1:
            return char
        return None

print(function('swiss'))
print(function('racecar'))
print(function('aabbcc'))