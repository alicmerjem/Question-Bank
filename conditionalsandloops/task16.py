"""
Write a program that receives 10 integers
and display their sum and average value
on the screen
"""

total = 0
count = 10

print("Please enter 10 integers: ")

for i in range(count):
    number = int(input("Enter integer " + str(1+i) + ": "))
    total += number

avg = total/count

print("Sum of the numbers: ", total)
print("Average: ", avg)