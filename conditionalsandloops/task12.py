"""
Write a program that will ask a user to
enter 2 numbers, first number is an 
integer and the second number is 
number of numbers that will be included
in the multiplication table
output:
e.g. 
x=15
no_numbers=10
15x1=15
15x2=30
15x3=45
15x4=60
15x5=75
15x6=90
15x7=105
15x8=120
15x9=135
15x10=150
"""

x = int(input("Enter the first number: "))
no_numbers = int(input("Enter the number of numbers: "))

for i in range(1, no_numbers + 1):
    print(x, "X", i, '=', x*i)