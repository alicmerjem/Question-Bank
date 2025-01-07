"""
Give 3 int values, a b and c. Return 
their sum. If one value is 13 then it 
does not count towards the sum and 
values to its right do not count. So 
if b i 13 then both b and c do not count.
"""

def lucky_sum(a, b, c):
    if a == 13:
        return b+c
    if b == 13:
        return a+c
    if c == 13:
        return a+b
    return a+b+c
