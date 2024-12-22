"""
a, b, c = 0, 0, 0
write a python program to print all 
permutations using those three 
variables

output : 000, 001, 002, 003, ... 999
"""

for a in range(10):
    for b in range(10):
        for c in range(10):
            print(a, b, c, end=", ")

