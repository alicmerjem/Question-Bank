"""
Given a number n, return true if n is
in range 1..10 inclusive. Unless
outside_mode is true, in which case
return True if the numbre is less or
equal to 1, or greater or equal to
10.
"""

def in1to10(n, outside_mode):
    if outside_mode:
        return n<=1 or n>=10
    else:
        return 1<= n <=10

print(in1to10(5, False))
print(in1to10(11, False))
print(in1to10(11, True))