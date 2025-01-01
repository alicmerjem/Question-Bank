"""
Write a program that will simulate 
hot and cold games. Target number is 
generated randomly when porgram and 
program should repeatedly ask the user
to enter his guess number. If his number
is smaller or greater than that number
+ 3, the program should output warm 
and in all other cases it should output
cold. display congrats your guess 
was right if the user enters the correct
number
"""

import random

# Generate a random target number between 1 and 100
target_number = random.randint(1, 100)

# Start the game loop
while True:
    # Ask the user for their guess
    guess = int(input("Enter your guess (between 1 and 100): "))
    
    # Check if the guess is correct
    if guess == target_number:
        print("Congratulations, your guess was right!")
        break
    # Check if the guess is within 3 units of the target number
    elif abs(guess - target_number) <= 3:
        print("Warm")
    else:
        print("Cold")
