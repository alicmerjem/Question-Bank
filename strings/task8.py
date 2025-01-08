"""
what is printed by the following
statements?
"""

animal = "alpaca"

print(animal[2:4])
print(animal[:4]+animal[2:])
print(animal[3:-1]*3)
print(animal[7:99]+animal[1:2])
print('t' in animal)

"""
1 - pa
2 - alpapaca
3 - acacac
4 - 1
5 - False
"""