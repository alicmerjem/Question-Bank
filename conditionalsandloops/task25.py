"""
Write a program that will ask users to
enter numbers repeatedly. output should
show the product of all even numbers
that the user enters and sum of all odd
numbers hat user enters. once the user
enters 0, the program stops asking the
user for more inputs.
"""

even_product = 1
odd_sum = 0 

while True:
    number = int(input("Enter a number, 0 to stop: "))
    
    if number == 0:
        break

    if number % 2 == 0:
        even_product *= number
    else:
        odd_sum += number

print("Product of even numbers: ", even_product)
print("Sum of odd numbers: ", odd_sum)
