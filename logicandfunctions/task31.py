"""
write a function to check whether a 
number is a harshad number or not. 
return true if yes, otherwise false. 
"""

def is_harshad(num):
    digit_sum = sum(int(digit) for digit in str(num))
    return num % digit_sum == 0
