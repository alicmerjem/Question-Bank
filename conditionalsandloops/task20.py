"""
Write a program that finds a number and
sum of of all numbers between x and y
which are divisible by z
"""

x = int(input("Enter the starting num: "))
y = int(input("Enter the ending num: "))
z = int(input("Enter the divisor: "))

count = 0
sum_num = 0

for number in range(x, y+1):
    if number%z==0:
        count+=1
        sum_num += number

print(f"Count of numbers divisible by {z} between {x} and {y}: {count}")
print(f"Sum of numbers between {x} and {y} divisible by {z}: {sum_num}")