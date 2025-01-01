"""
Write a program to check whether a 
number can be expressed as a sum of two
prime numbers
"""

def is_prime(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
        return True

def check_sum(number):
    for i in range(2, number):
        if is_prime(i) and is_prime(number-i):
            return True, i, number-i
        return False, None, None

num = int(input("Enter a number: "))

result, prime1, prime2 = check_sum(num)

if result:
    print(f"{num} can be expressed as the sum of {prime1} and {prime2}.")
else:
    print(f"{num} cannot be expressed as the sum of two prime numbers.")