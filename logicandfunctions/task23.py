"""
A happy number is defined by the
following process: starting with any
positive integer, replace the number 
by the sum of squares of its digits,
and repeat the process until the num
equals to 1. those nums for which this 
process ends in 1 are happy numbers,
whule those that do not end in 1 are 
unhappy numbers. write a function to 
check whether a number is happy or not
"""
def is_happy(num):
    seen = set()
    while num!= 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit)**2 for digit in str(num))

    return num == 1
print(is_happy(7))
print(is_happy(932))
print(is_happy(6))