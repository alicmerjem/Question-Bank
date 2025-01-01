"""
Write a program that asks the user to
enter a number of rows and then the 
program should output Floyd's triangle

e.g.
number of rows = 5
output:
1
01
101
0101
10101
"""

rows = int(input("Enter the number of rows: "))

current_number = 1

# loop through the number of rows
for i in range(1, rows+1):
    # for each row print the numbers
    # j is current position within the row
    for j in range(i):
        print(current_number, end="")
        current_number = 1 if current_number == 0 else 0
    
    print()