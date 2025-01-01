"""
Write a program that asks the user to
enter a number and then print all
perfect numbers from 0 all the way to
the entered number 
perfect number - positive number whose
sum of all positive divisors excluding
that number is equal to that number
e.g.  6 divisors 1 2 and 3, 
6 = 1+2+3
"""

def is_perfect(number):
    # initialize sum of divisors
    divisor_sum = 0

    # loop through possible divisors
    for i in range(1, number):
        if number % i == 0:
            divisor_sum += i

    # check if the sum of divisors is equal to the number
    return divisor_sum == number

max_number = int(input("Enter a number: "))

print("Perfect numbers from 0 to", max_number, "are:")
for num in range(1, max_number + 1):
    if is_perfect(num):
        print(num)
