"""
Write a Python program to display the
sign of chinese zodiac for a given 
year in which you were born
"""

def chinese_zodiac(year):
    zodiac_signs = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]

    index = (year - 1900) % 12

    return zodiac_signs[index]

birth_year = int(input("Enter your birth year: "))

zodiac_sign = chinese_zodiac(birth_year)
print("Your Chinese Zodiac sign is: ", zodiac_sign)