"""
write a function that for 3 given
intergers a b and c return true if it
is possible to add two of them to get
the third
"""

def twoAsOne(a, b, c):
    return a + b == c or a + c == b or b + c == a

print(twoAsOne(1, 2, 3))
print(twoAsOne(3, 1, 2))
print(twoAsOne(3, 2, 3))