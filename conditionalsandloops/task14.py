"""
Write a program that asks the user to
enter one number and then display the
factorial of that number
"""

import math

user = int(input("Enter a number: "))

factorial = math.factorial(user)

print("The factorial is: ", factorial)