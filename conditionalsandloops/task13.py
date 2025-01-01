"""
Write a program that will continuously
ask users to enter numbers. Once the user
types "done" the program should stop 
asking for more numbers and display
the sum of all the numbers that user
entered
"""

total = 0

while True:
    user = input("Enter a number (done to finish): ")
    if user == "done":
        break
    try:
        total+=float(user)
    except ValueError:
        print("Invalid input.")

print("The sum of all numbers comes out to: ", total)