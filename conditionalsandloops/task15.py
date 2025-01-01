"""
Write a program that asks the user to
enter one number and then display the
fibonacci sequence for that number
"""

n = int(input("Enter a number: "))

a = 0
b = 1

print("Fibonacci sequence: ")
while a<=n:
    print(a, end="")
    a, b= b, a+b