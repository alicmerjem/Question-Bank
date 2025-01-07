"""
write a function which will find all
such numbers which are divisible by 7
but are not a multiple of 5, between
numbers a and b (both included)
"""

def divisible_7_not_5(a, b):
    return [i for i in range(a, b+1) if i%7==0 and i%5!=0]
