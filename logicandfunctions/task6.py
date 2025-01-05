"""
You are driving a little too fast, and
a police officer stops you. Write code
to compute the result, encoded as int
value: 
0 - no ticket 
1 - small ticket
2 - big ticket
If the speed is 60 or less, you get 0.
If the speed is between 61 and 80,
inclusive, you get 1.
If the speed is 81 or more, you get
2. 
Unless it is your bday, on that day you
can go 5 over.
"""

def caught_speeding(speed, is_bday):
    if is_bday:
        speed_limit = 5
    else:
        speed_limit = 0
    
    if speed <=60 + speed_limit:
        return 0
    if speed <= 80 + speed_limit:
        return 1
    else:
        return 2

print(caught_speeding(60, False))  # → 0 (no ticket)
print(caught_speeding(65, False))  # → 1 (small ticket)
print(caught_speeding(65, True))   # → 0 (no ticket because it's your birthday)
print(caught_speeding(85, True))   # → 1 (small ticket, birthday speed is allowed up to 85)
print(caught_speeding(90, False))  # → 2 (big ticket)
