"""
Write a function that will return 
number of even digits smaller than 7
in an integer
"""

def count_even_digits(num):
    return sum(1 for digit in str(num) if int(digit)%2==0 and int(digit)<7)

