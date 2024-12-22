"""
Write a Python program that accepts a
string and calculate the number of 
digits and letters
"""

input_string = input("Enter a string: ")

digits_count = 0
letters_count = 0

for char in input_string:
    if char.isdigit():
        digits_count += 1
    elif char.isalpha():
        letters_count += 1

print("Number of digits: ", digits_count)
print("Number of letters: ", letters_count)