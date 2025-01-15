"""
given a string, write a function to
return a rotated left 2 version where
the first 2 chars are moved to the end.
the string length will be at least 2
"""
def left2(s):
    return s[2:] + s[:2]

print(left2('Hello'))
print(left2('java'))
print(left2('hi'))