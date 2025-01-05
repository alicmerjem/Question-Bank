"""
Given a non negative number num, return
True if num is iwhtin 2 of a multiple
of 10. Note:
(a%b) is the remainded of dividing a by b.
so (7%5) is 2
"""

def near_ten(num):
    return num % 10 in [8, 9, 0, 1, 2]

print(near_ten(12))
print(near_ten(17))
print(near_ten(19))