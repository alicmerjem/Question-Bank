"""
Lilly is N years old. For each bday she
receives a present. For each odd bday
(1, 3, 5, .., n) she  gets toys and
for each even bday (2, 4, 6, ..., n) 
sge gets money. For her second bday she
got 10.00 USD and the amount is increased
by 10.00 USD for each following bday.
Over the years Lilly has secretly 
saved her money. Lilly's brother, in 
the years when she received money, took
1.00 USD from each of the amounts.
Lilly has sold the toys she got over
the years and each one for P USD and
added the sum to the amount of saved 
money. W/ the money she wanted to buy
a washing machine for X USD. Write
a program that calculated how much 
money she has saved and if its enough
to buy a washing machine 
"""

def calculate_savings(n, P, X):
    # initialize savings
    savings = 0
    
    # calculate savings for even birthdays (money)
    for i in range(2, n + 1, 2):  # i will go over even numbers 2, 4, 6, ..., n
        amount_received = i * 10  # 10 USD multiplied by the birthday number
        amount_after_brother_takes = amount_received - 1  # Brother takes 1 USD
        savings += amount_after_brother_takes  # Add to savings
    
    # Calculate savings from odd birthdays (toys)
    for i in range(1, n + 1, 2):  # i will go over odd numbers 1, 3, 5, ..., n
        savings += P  # Add P USD from selling the toy
    
    # Check if savings are enough to buy the washing machine
    if savings >= X:
        return f"Lilly has saved enough money: {savings:.2f} USD, which is enough to buy the washing machine!"
    else:
        return f"Lilly has saved {savings:.2f} USD, which is not enough to buy the washing machine."

# Input from the user
n = int(input("Enter Lilly's age (in years): "))
P = float(input("Enter the price of each toy in USD: "))
X = float(input("Enter the price of the washing machine in USD: "))

# Calculate and display the result
result = calculate_savings(n, P, X)
print(result)
