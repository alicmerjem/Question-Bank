"""
Write a program that asks the user to
enter one numebr and then display the 
sum of all even/odd numbers from 0
to the number that user entered
"""

number = int(input("Enter a number: "))

even_sum = 0
odd_sum = 0

for i in range(number + 1):
    if i%2 == 0:
        even_sum +=i
    if i%3==0:
        odd_sum += i

print("The sum of even numbers is: ", even_sum)
print("The sum of odd numbers is: ", odd_sum)