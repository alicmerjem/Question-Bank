"""
write a function to find whether a given
number is a disarium number.
a disarium number is a num defined by
the following proccess:
sum of its digits powered with their 
respective position is equal to the 
original number. for example 175
isa disarium number as 1^1 + 7^2 + 5^3
= 135
"""

def is_disarium(num):
    num_str = str(num)
    return num == sum(int(digit) ** (1+i) for i, digit in enumerate(num_str))
