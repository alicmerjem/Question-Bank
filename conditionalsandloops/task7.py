"""
Write a Python program to find numbers
between 100 and 400 (both included)
where each digit of a number is an
even number. the numbers obtained should
be printed in a comma-separated sequence
"""

def all_even_digits(number):
    for digit in str(number):
        if int(digit)%2!=0:
            return False
        return True

result = []
for num in range(100, 401):
    if all_even_digits(num):
        result.append(str(num))

print(",".join(result))